from django import forms

from .models import Properties, PropertiesPhotos

from django.forms.models import inlineformset_factory


class PropertiesForm(forms.ModelForm):
    # then telling which model should be used to create this form

    class Meta:
        model = Properties
        fields = ('title', 'prop_type', 'city', 'neighborhood',
                  'category', 'description', 'price', 'size', 'yt_url', 'position',)

    def signup(self, request, prop):
        prop.prop_photo = self.cleaned_data['prop_photo']
        prop.save()
PropertiesFormSet = inlineformset_factory(
    Properties, PropertiesPhotos, can_delete=False, exclude=['img_height', 'img_width', 'prop'])
