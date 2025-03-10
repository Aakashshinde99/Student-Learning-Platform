# 🚀 Student Learning Platform (AI-Powered Study Roadmap)
Automatically Generate Study Plans for Any Exam Using AI (Gemini API)  
✅ **Personalized Roadmap Generation 🚀** | ✅ **Time-Based Task Schedules ⏳** | ✅ **User Authentication 👤**  

---

## 📜 Project Description
This project is a **Student Learning Platform** that allows students to:  

✅ **Create a study plan** by providing their **Exam Name** and **Exam Date**.  
✅ **Use Google Gemini AI API** to auto-generate a complete Study Roadmap.  
✅ Track daily study tasks like: **Morning, Afternoon, Evening**.  
✅ **Mark tasks as complete/incomplete** and stay on track.  
✅ **Login/Register** functionality for personalized access.  

---

## 📊 Project Features
| Feature | Status |
|---------|--------|
| ✅ **User Registration/Login** | Fully Working ✔️ |
| ✅ **AI-Generated Study Plan** | Fully Working ✔️ |
| ✅ **Track Study Progress** | Fully Working ✔️ |
| ✅ **Personalized Roadmap** | Fully Working ✔️ |
| ✅ **Daily Tasks (Morning, Afternoon, Evening)** | Fully Working ✔️ |
| ✅ **Dynamic Date Tracking** | Fully Working ✔️ |
| ✅ **Task Completion Status** | In Progress 🟡 |
| ✅ **Responsive Design (Bootstrap)** | Fully Working ✔️ |  

---

## 💻 Tech Stack Used
This project was built using the following technologies:  

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.13.2 | Core Programming Language |
| **Django** | 5.1.6 | Backend Web Framework |
| **Google Gemini AI API** | 1.5.0 | AI Roadmap Generator |
| **SQLite3** | Default | Database Storage |
| **Bootstrap 5.3** | Latest | Frontend Design |  

---

## 💡 How Does This Project Work?
The entire project workflow is like this:  

✅ **Step 1:** User Registers/Login.  
✅ **Step 2:** User creates a Study Plan by entering:  
- 📅 **Exam Name** (e.g. DSA Interview, Web Dev Test).  
- ⏳ **Exam Date** (e.g. March 14, 2025).  
✅ **Step 3:** The app will:  
- 💡 Automatically call **Gemini AI API**.  
- 📅 Generate **Day-wise Study Plan** (like **Day 1, Day 2, Day 3...**).  
- ✅ Save it to **Database (SQLite3)**.  
✅ **Step 4:** User can:  
- ✅ View their **Study Roadmap**.  
- ✅ Track tasks like:  
  - **Morning Task ✅**  
  - **Afternoon Task ✅**  
  - **Evening Task ✅**  
✅ **Step 5:** User can complete tasks or keep them pending.  
✅ 💯 AI-Powered Study Plan in seconds! 🚀  

---

## 🎉 Project Output Screenshots
Here are the main screenshots of the project:  
📸 **1. Login Page**  
📸 **2. Create Study Plan**  
📸 **3. AI-Generated Roadmap**  
📸 **4. View Study Progress**  

---
## Make sure you create Gemini API Key

## ✅ How To Run This Project Locally
Follow these simple steps to run the project on your local machine.  

### 💻 Step 1: Clone the Repository
Open your terminal and run:  

```bash
git clone https://github.com/your-username/student-learning-platform.git
cd student-learning-platform
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
