from django.db import models
from accounts.models import CompReg,CanReg
from accounts.models import UserType

# Create your models here.

class JobDetails(models.Model):

    comp = models.ForeignKey(CompReg,on_delete=models.CASCADE,null=True)
    jtype = models.CharField(max_length=50,null=True)
    jtitle = models.CharField(max_length=50,null=True)
    clength = models.CharField(max_length=30,null=True)
    salary = models.CharField(max_length=20,null=True)
    time = models.DateTimeField(auto_now=True)
    qualreq = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=900,null=True)
    hide = models.BooleanField(null=True,default=0)
    wrkexp = models.CharField(null=True,max_length=30)
    jobreq = models.CharField(null=True,max_length=500)

class JobsApplied(models.Model):
    cand = models.ForeignKey(CanReg,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails,on_delete=models.CASCADE)
    com = models.ForeignKey(CompReg,on_delete=models.CASCADE,null=True)
    selected = models.CharField(max_length=10,null=True)
    rejected = models.CharField(max_length=10,null=True)
    message = models.CharField(max_length=50,null=True)

class FeedBack(models.Model):
    candidate = models.ForeignKey(CanReg,on_delete=models.CASCADE,null=True)
    company = models.ForeignKey(CompReg,on_delete=models.CASCADE,null=True)
    usertype = models.ForeignKey(UserType,on_delete=models.CASCADE,null=True)
    feedback = models.CharField(max_length=500,null=True)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    reply = models.CharField(max_length=250,null=True,default="not viewed")


class JobReport(models.Model):
    candidate = models.ForeignKey(CanReg,on_delete=models.CASCADE,null=True)
    jobs = models.ForeignKey(JobsApplied,on_delete=models.CASCADE,null=True)
    report = models.FileField('files/',null=True)
    message = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=100,null=True)



