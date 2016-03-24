from django import forms

from .models import Properties


class PropertiesForm(forms.ModelForm):
	#then telling which model should be used to create this form
	class Meta:
		model = Properties

		fields = ('title', 'prop_type', 'city', 'neighborhood', 'category', 'description', 'price', 'size','yt_url')