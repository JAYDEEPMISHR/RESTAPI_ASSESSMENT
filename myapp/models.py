from django.db import models

# Create your models here.

class Snippet(models.Model):
	title= models.CharField(max_length=100,blank=True)
	code=models.TextField(blank=True)
	linenos=models.BooleanField(blank=True)
	language=models.CharField(max_length=100,blank=True)
	style=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.title
