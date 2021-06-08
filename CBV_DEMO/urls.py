"""CBV_DEMO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base.as_view(),name="homepage"),

    path('schools/',views.School_ListView.as_view(),name="school_list"), #check cap's or not
    path('schools/<int:pk>',views.School_DetailView.as_view(),name="detail_view"),
    path('schools/create/',views.Create_School.as_view(),name="create_school"),
    path('schools/update/<int:pk>',views.Update_School.as_view(),name="update_school"),
    path('schools/delete/<int:pk>',views.Delete_School.as_view(),name="delete_school"),

    path('students/',views.Student_ListView.as_view(),name="student_list"),  # check cap's or not
    path('students/<int:pk>',views.Student_DetailView.as_view(),name="studentdetail_view"), #carefull! dont give same names for url. because it will override. better divide the names.
    path('students/create/',views.Create_Student.as_view(),name="create_student"),  
    path('students/update/<int:pk>',views.Update_Student.as_view(),name="update_student"),
    path('students/delete/<int:pk>',views.Delete_Student.as_view(),name="delete_student"),

 ]
