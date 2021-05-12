from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Pratice_Problems
class Pratice_Problems(models.Model):
    title = models.CharField(max_length=100,null=True)
    long_des = models.TextField(null=True)
    image = models.FileField(null=True, blank=True)
    inputt1 = models.TextField(null=True, blank=True)
    ex_outputt1 = models.TextField(null=True, blank=True)
    inputt2 = models.TextField(null=True, blank=True)
    ex_outputt2 = models.TextField(null=True, blank=True)
    inputt3 = models.TextField(null=True, blank=True)
    ex_outputt3 = models.TextField(null=True, blank=True)
    inputt4 = models.TextField(null=True, blank=True)
    ex_outputt4 = models.TextField(null=True, blank=True)
    inputt5 = models.TextField(null=True, blank=True)
    ex_outputt5 = models.TextField(null=True, blank=True)
    inputt6 = models.TextField(null=True, blank=True)
    ex_outputt6 = models.TextField(null=True, blank=True)
    inputt7 = models.TextField(null=True, blank=True)
    ex_outputt7 = models.TextField(null=True, blank=True)
    inputt8 = models.TextField(null=True, blank=True)
    ex_outputt8 = models.TextField(null=True, blank=True)
    inputt9 = models.TextField(null=True, blank=True)
    ex_outputt9 = models.TextField(null=True, blank=True)
    inputt10 = models.TextField(null=True, blank=True)
    ex_outputt10 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class User_Pratice_Solution(models.Model):
    usr_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    solution_to_problem = models.ForeignKey(Pratice_Problems, on_delete=models.CASCADE,null=True)
    status = models.BooleanField(null=True, default=False)
    code_for_problem = models.TextField(null=True)
    point_scored = models.IntegerField(null=True,blank=True)
    outputt1 = models.TextField(null=True, blank=True)
    outputt2 = models.TextField(null=True, blank=True)
    outputt3 = models.TextField(null=True, blank=True)
    outputt4 = models.TextField(null=True, blank=True)
    outputt5 = models.TextField(null=True, blank=True)
    outputt6 = models.TextField(null=True, blank=True)
    outputt7 = models.TextField(null=True, blank=True)
    outputt8 = models.TextField(null=True, blank=True)
    outputt9 = models.TextField(null=True, blank=True)
    outputt10 = models.TextField(null=True, blank=True)

    def __int__(self):
        return [self.id,self.usr_name]


class All_Contest_Data(models.Model):
    title = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.title

class Contest_Questions(models.Model):
    contest_id = models.ForeignKey(All_Contest_Data,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    long_des = models.TextField(null=True)
    image = models.FileField(null=True, blank=True)
    inputt1 = models.TextField(null=True, blank=True)
    ex_outputt1 = models.TextField(null=True, blank=True)
    inputt2 = models.TextField(null=True, blank=True)
    ex_outputt2 = models.TextField(null=True, blank=True)
    inputt3 = models.TextField(null=True, blank=True)
    ex_outputt3 = models.TextField(null=True, blank=True)
    inputt4 = models.TextField(null=True, blank=True)
    ex_outputt4 = models.TextField(null=True, blank=True)
    inputt5 = models.TextField(null=True, blank=True)
    ex_outputt5 = models.TextField(null=True, blank=True)
    inputt6 = models.TextField(null=True, blank=True)
    ex_outputt6 = models.TextField(null=True, blank=True)
    inputt7 = models.TextField(null=True, blank=True)
    ex_outputt7 = models.TextField(null=True, blank=True)
    inputt8 = models.TextField(null=True, blank=True)
    ex_outputt8 = models.TextField(null=True, blank=True)
    inputt9 = models.TextField(null=True, blank=True)
    ex_outputt9 = models.TextField(null=True, blank=True)
    inputt10 = models.TextField(null=True, blank=True)
    ex_outputt10 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title