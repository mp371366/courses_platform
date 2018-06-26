from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<int:course_id>', views.course, name='course'),
]
