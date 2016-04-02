from django import forms
from .models import Subscribtions
from properties.models import PROPERTIES_CATEGORIES, PROPERTIES_TYPES,STATUS
from cities_light.models import City, Region
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class SubscribtionsForm(forms.Form):
	#then telling which model should be used to create this form
	city = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
	neighborhood = forms.ModelChoiceField(queryset=City.objects.all(), required=False)
	property_type = forms.ChoiceField(choices=PROPERTIES_TYPES, widget=forms.Select(), required=False)
	property_categories = forms.ChoiceField(choices=PROPERTIES_CATEGORIES, widget=forms.Select(), required=False)
	min_price = forms.IntegerField(min_value=0, required=False)
	max_price = forms.IntegerField(min_value=0, required=False)
	status = forms.ChoiceField(choices=STATUS, widget=forms.Select(), required=False)
	def __init__(self, *args, **kwargs):
		super(SubscribtionsForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'subscribtions_form'
		self.helper.form_method = 'get'
		self.helper.form_action = 'add_subscribtion/'
		self.helper.form_class = 'form-inline'
		self.helper.field_template = 'bootstrap3/layout/inline_field.html'
		self.helper.layout = Layout(
			Field('city'),
            Field('neighborhood'),
            Field('property_type'),
            Field('property_categories'),
            Field('min_price'),
            Field('max_price'),
            Field('status'),
        )
		self.helper.add_input(Submit('submit', 'Submit'))


    #def subscribtions(self, request, sub):
     #   sub.city = self.cleaned_data['city']
      #  sub.neighborhood = self.cleaned_data['neighborhood']
       # sub.property_type = self.cleaned_data['property_type']
       # sub.property_categories = self.cleaned_data['property_categories']
       # sub.min_price = self.cleaned_data['min_price']
        #sub.max_price = self.cleaned_data['max_price']
	#sub.status = self.cleaned_data['status']
     #   sub.save()

# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())

#     def clean(self):
#         subname = self.cleaned_data.get('subname')
#         password = self.cleaned_data.get('password')
#         sub = authenticate(subname=subname, password=password)
#         if not sub:
#             raise forms.ValidationError("Sorry,")
#         return self.cleaned_data

#     class Meta:
#         model = sub
#         fields = ['subname', 'password']


# subCreationFormset = inlineformset_factory(
#     sub, subProfile, can_delete=False, exclude=['points', 'social_media',
#                                                   'messages', 'img_height', 'img_width'])
