from distutils.command.upload import upload
from django.db import models
# Create your models here.

class Projects(models.Model):
    name=models.CharField(max_length=250,null=True)
    image=models.ImageField(upload_to="media/projects/")
    link=models.CharField(max_length=250,null=True)

    def __str__(self) -> str:
        return self.name[0:11]



class Certificates(models.Model):
    name=models.CharField(max_length=250)
    certi=models.ImageField(upload_to="media/certificates/")

    def __str__(self) -> str:
        return self.name[0:11]


class Contacts(models.Model):
    icon=models.ImageField(upload_to="media/contacts/")
    link=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.link[0:11]