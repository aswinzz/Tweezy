from django.db import models

class Document(models.Model):
    username=models.CharField(maxlength=200,default="")