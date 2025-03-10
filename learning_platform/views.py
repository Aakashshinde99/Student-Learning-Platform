import google.generativeai as genai
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from .models import Schedule, Task
from .forms import ScheduleForm
from datetime import timedelta
from django.contrib import messages


# ✅ Ensure API key is loaded
if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)
else:
    raise ValueError("❌ GEMINI_API_KEY is not set! Check your .env file.")

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# ✅ REGISTER USER
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # ✅ Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        # ✅ Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # ✅ Auto login after registration
        login(request, user)
        return redirect('/')

    return render(request, 'register.html')


# ✅ LOGIN USER
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # ✅ Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('/login/')

    return render(request, 'login.html')


# ✅ LOGOUT USER
def user_logout(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard(request):
    schedules = Schedule.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'schedules': schedules})


@login_required
def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()

            # ✅ Generate Study Plan Based on Days Remaining
            generate_study_plan(schedule)
            return redirect('dashboard')
    else:
        form = ScheduleForm()
    return render(request, 'create_schedule.html', {'form': form})


@login_required
def view_roadmap(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id, user=request.user)
    tasks = Task.objects.filter(schedule=schedule)
    return render(request, 'view_roadmap.html', {
        'schedule': schedule,
        'tasks': tasks
    })


@login_required
def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id, user=request.user)
    schedule.delete()
    messages.success(request, "✅ Schedule Deleted Successfully!")
    return redirect('dashboard')


import re
from datetime import timedelta
from django.utils.timezone import now
from .models import Task

def generate_study_plan(schedule):
    # ✅ Convert dates
    today_datetime = now()
    exam_datetime = schedule.exam_date

    # ✅ Days remaining logic
    days_remaining = (exam_datetime - today_datetime).days
    if days_remaining <= 0:
        days_remaining = 1

    # ✅ Gemini API Prompt
    prompt = f"""
    I have an upcoming exam called "{schedule.exam_name}" on {schedule.exam_date}.
    I have {days_remaining} days left to study.
    Create a detailed study plan divided by days like:

    Day 1: Topic 1
    Day 2: Topic 2
    Day 3: Topic 3
    """

    # ✅ Call Gemini API
    model = genai.GenerativeModel('gemini-1.5-flash-001')
    response = model.generate_content(prompt)
    study_plan = response.text.strip()

    # ✅ Step 1: Split the text by "Day X"
    day_blocks = re.split(r'(Day \d+)', study_plan)

    # ✅ Step 2: Loop through and capture Day + Content
    tasks = []
    current_day = None
    for block in day_blocks:
        block = block.strip()
        if block.startswith("Day"):
            current_day = block
        elif current_day:
            # ✅ Combine the current day and the content
            tasks.append({
                'day': current_day,
                'content': block
            })

    # ✅ Step 3: Create Tasks based on Days
    study_date = today_datetime.date()
    for task in tasks:
        # ✅ Stop creating tasks if we pass the exam date
        if study_date > exam_datetime.date():
            break

        # ✅ Create Task in DB
        Task.objects.create(
            schedule=schedule,
            topic=f"{task['day']}\n\n{task['content']}",
            practice_time=study_date
        )

        # ✅ Move to next day
        study_date += timedelta(days=1)

    # ✅ If tasks exceeded, print a warning
    if study_date > exam_datetime.date():
        print("⚠️ Warning: Tasks exceeded the exam date.")
