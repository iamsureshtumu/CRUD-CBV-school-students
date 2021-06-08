from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DeleteView,TemplateView,ListView,UpdateView,DetailView,CreateView
from myapp.forms import *
from myapp.models import School,Student
from django.urls import reverse,reverse_lazy
#Basic View
# Create your views here.

class base(TemplateView):
    template_name='base.html'

class School_ListView(ListView):
    model=School
    template_name="school_list.html"
    context_object_name="schools"

class Student_ListView(ListView):
    model=Student
    template_name="myapp/student_list.html"
    context_object_name="students"

class Student_DetailView(DetailView):
    model=Student
    template_name='myapp/student_detail.html'
    context_object_name="student_detail"

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})

class School_DetailView(DetailView):
    model=School
    template_name='school_detail.html'
    context_object_name="school_detail"

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})


class Create_School(CreateView):
    model=School
    template_name="school_form.html"
    fields=('name','principal','location')

class Create_Student(CreateView):
    model=Student
    fields=('name','age','school')

class Update_School(UpdateView):
    model=School
    template_name="school_form.html"
    fields=('name','principal','location')

class Update_Student(UpdateView):
    model=Student
    fields=('name','age','school')

class Delete_School(DeleteView):
    model=School
    template_name="delete_school.html"
    success_url=reverse_lazy('school_list')
    
class Delete_Student(DeleteView):
    model=Student
    template_name="myapp/delete_student.html"
    success_url=reverse_lazy('student_list')

# class Delete_Student(DeleteView):
#     model=Student
#     success_url = reverse_lazy("studentlist")



