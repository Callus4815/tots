from django.db import models

# Create your models here.


class profile(models.Model):
	name = models.CharField(max_length=1200)
	description = models.TextField(default="Description Here")


	def __str__(self):
		return self.name