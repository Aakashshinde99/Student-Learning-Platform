from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import json

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=200)
    exam_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exam_name


class Task(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    topic = models.TextField()  # This will store JSON
    practice_time = models.DateField()
    status = models.BooleanField(default=False)  # Completed or not

    def get_json(self):
        return json.loads(self.topic)


class Reminder(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    remind_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.task.topic}"
