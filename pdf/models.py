from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    summary=models.TextField(max_length=2000)
    degree=models.CharField(max_length=1000)
    school=models.CharField(max_length=200)
    university=models.CharField(max_length=1000)
    previous_work=models.CharField(max_length=1000)
    skills=models.CharField(max_length=1000)
    portfolio_url=models.CharField(max_length=500)
    linkedin_url=models.CharField(max_length=500)
    github_url=models.CharField(max_length=500)
    projects=models.TextField()
    hobbies=models.CharField(max_length=500)
    certications=models.TextField()