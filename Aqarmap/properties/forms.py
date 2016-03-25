from django import forms

from .models import Properties, PropertiesPhotos


class PropertiesForm(forms.ModelForm):
	#then telling which model should be used to create this form
	class Meta:
		model = Properties
		fields = ('title', 'prop_type', 'city', 'neighborhood', 'category', 'description', 'price', 'size','yt_url','position')
#another form for the PropertiesPhotos
# class PropertiesPhotosForm(forms.ModelForm):
# 	class Meta:
# 		model = PropertiesPhotos
# 		fields = ('prop_photo')
