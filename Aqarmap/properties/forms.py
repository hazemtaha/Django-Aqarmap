from django import forms

from .models import Properties, PropertiesPhotos

from django.forms.models import inlineformset_factory

class PropertiesForm(forms.ModelForm):
	#then telling which model should be used to create this form
	class Meta:
		model = Properties
		fields = ('owner','title', 'prop_type', 'city', 'neighborhood', 'category', 'description', 'price', 'size','yt_url','position')

PropertiesFormSet = inlineformset_factory(
	Properties, PropertiesPhotos, can_delete=False, fields=['prop_photo'])