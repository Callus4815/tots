from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('photo', 'name', 'brand', 'category', 'size', 'price', 'text')

class ItemImageForm(forms.Form):
	image = forms.FileField(label="Select an image")