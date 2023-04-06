from django.db import models


#PROJECT CHOICE
CHOICE = (
    ("SQL","SQL"),
    ("PYTHON","PYTHON"),
    ("DATA_VISUALIZATION","DATA_VISUALIZATION")

)
# Create your models here.
class Projects(models.Model):
    Project_Title = models.CharField(max_length=50)
    Project_Type = models.CharField(max_length=50,choices=CHOICE)
    Project_Desc = models.TextField(default="")
    Project_img = models.ImageField(upload_to='upload_img')
    Project_Live_Link = models.CharField(max_length=200,default="")
    Project_github_Link = models.CharField(max_length=200,default="")


    def __str__(self):
        return self.Project_Title


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=200)
    Message = models.TextField()
    
    def __str__(self):
        return self.Subject + " " + "Message From "+ self.Name

class Certification(models.Model):
    cer_name = models.CharField(max_length=50)
    cer_org = models.CharField(max_length=50)
    cer_details = models.CharField(max_length=200)
    cer_img = models.ImageField(upload_to='certifications')

    def __str__(self):
        return self.cer_name
    