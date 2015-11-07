from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Item(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=255)
	brand = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	size = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	condition = models.CharField(max_length=255)
	text = models.CharField(max_length=140)
	photo = models.ImageField(upload_to='item/%Y/%m/%d')
	posted_at = models.DateTimeField()
	favorited_items = models.ManyToManyField(User, through='Favorite',
												related_name="favorited_items")

	def get_absolute_url(self):
		return reverse('show_item', kwargs={'item_id': self.id})


	def __str__(self):
		return "{}: {}: {}".format(self.user, self.name, self.text)


class Favorite(models.Model):
	user = models.ForeignKey(User)
	item = models.ForeignKey(Item)

	def __str__(self):
		return "{} --> {}".format(srlf.user, self.item)
	                                   
