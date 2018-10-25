from django.db import models

class Document(models.Model):
    csvFile = models.FileField(upload_to='documents/',default='dummy.txt')