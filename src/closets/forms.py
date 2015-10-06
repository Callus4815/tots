from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'brand', 'category', 'size', 'price', 'text', 'photo')

class ItemImageForm(forms.Form):
	image = forms.FileField(label="Select an image")