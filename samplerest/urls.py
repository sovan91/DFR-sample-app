from django.contrib import admin
from django.urls import path
from restapp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',views.employeesList.as_view()),
    path('Student/',views.StudentList.as_view()),
]
