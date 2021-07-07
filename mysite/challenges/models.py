from django.db import models


class Solution(models.Model):
	challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
	text = models.TextField()

# Create your models here.
class Challenge(models.Model):
	LANG_CHOICES=(
		('python','Python'),
		('c#','C#'),
		('c++','C++'),
		('java','Java'),
		('javascript','Javascript'),
		('php','PHP'),
		('ruby','Ruby'),
		('swift','Swift'),
	)
	c_id = models.CharField(max_length=200, default='')
	lang = models.CharField(max_length=40, default='python', choices =LANG_CHOICES)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	desc = models.TextField(blank=True)
	instructions = models.TextField(blank=True)
	tags = models.CharField(max_length=200)
	difficulty = models.CharField(max_length=200)
	

