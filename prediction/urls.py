from django.contrib import admin
from django.urls import path
from prediction import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),  # Home page
    path("predictions/", views.prediction, name="prediction"),  # Prediction page
    path('district/<str:district_name>/', views.district_detail, name='district_detail'), # District detail page
    path("response-plan/", views.response, name="response"),  # Response plan page
    path("resource/", views.resource, name="resource"), # Resource plan page
    path("chatbot_api/", views.chatbot_api, name="chatbot_api"),  # Chatbot API endpoint
]
