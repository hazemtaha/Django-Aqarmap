from django import forms
from accounts.models import UserProfile
from cities_light.models import Country
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
# from crispy_forms.bootstrap import StrictButton


class UserSettingForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name',
                  'gender', 'country', 'default_currency',
                  'phone_number', 'account_type', '_image']

    def __init__(self, *args, **kwargs):
        super(UserSettingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'settings_form'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'settings:user_setting'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.add_input(Submit('submit', 'Submit'))
