from django import forms
from .models import Subscribtions

    class SubscribtionsForm(forms.ModelForm):
	#then telling which model should be used to create this form
	class Meta:
		model = Subscribtions
		fields = ('city', 'neighborhood', 'property_type', 'property_categories', 'min_price', 'max_price', 'status')

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
