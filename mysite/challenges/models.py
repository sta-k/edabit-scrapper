from django.db import models

# Create your models here.
class Challenge(models.Model):
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	desc = models.TextField(blank=True)
	tags = models.CharField(max_length=200)
	difficulty = models.CharField(max_length=200)
	

