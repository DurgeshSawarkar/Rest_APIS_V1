from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.studentsView , name='studentsView'),
    path('student/<int:pk>/', views.studentDetailView , name='studentDetailView'),

    path('employee/', views.Employees.as_view()),
    path('employee/<int:pk>/', views.EmmployeesDetail.as_view()),
]
