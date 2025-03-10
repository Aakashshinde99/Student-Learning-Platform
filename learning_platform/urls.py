from django.urls import path
from .views import (
    dashboard, 
    create_schedule, 
    view_roadmap, 
    register_user, 
    user_login, 
    user_logout,
    delete_schedule
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('create/', create_schedule, name='create_schedule'),
    path('roadmap/<int:schedule_id>/', view_roadmap, name='view_roadmap'),
    path('delete/<int:schedule_id>/', delete_schedule, name='delete_schedule'),


    # ✅ User Authentication URLs
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
