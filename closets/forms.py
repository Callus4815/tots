from django import forms

from closets.models import Item


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('photo', 'name', 'brand', 'category', 'size', 'price', 'text')
