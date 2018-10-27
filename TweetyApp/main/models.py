from django.db import models

class Document(models.Model):
    username=models.CharField(max_length=200,default="")