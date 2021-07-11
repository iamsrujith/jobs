from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class CompReg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(null=True,max_length=50)
    address = models.CharField(max_length=50,null=True)
    place = models.CharField(max_length=50,null=True)
    NofEmp = models.IntegerField(null=True)
    RegDate = models.IntegerField(null=True)
    Desc = models.CharField(max_length=500,null=True)
    logo = models.ImageField('images/',null=True)
    rnum = models.CharField(max_length=40,null=True)
    comtype = models.CharField(max_length=50,null=True)

class CanReg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(null=True,max_length=50)
    address = models.CharField(null=True,max_length=60)
    place = models.CharField(null=True,max_length=30)
    desc = models.CharField(max_length=250,null=True)
    photo = models.ImageField('images/',null=True)
    resume = models.FileField('resumes/',null=True)
    qual = models.CharField(null=True,max_length=50)
    workexp = models.CharField(null=True,max_length=300)
    skills = models.CharField(null=True,max_length=100)
    gender = models.CharField(null=True,max_length=10)
    others = models.CharField(null=True,max_length=100)
# class VolReg(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     phone_no = models.CharField(null=True,max_length=50)
#     address = models.CharField(max_length=50)
#
#
# class HotelReg(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     phone_no = models.CharField(null=True,max_length=50)
#     address = models.CharField(max_length=50)
#     place = models.CharField(max_length=50,null=True)
#
# class donor_reg(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_no = models.CharField(null=True,max_length=50)
#     address = models.CharField(max_length=50)


