from django import forms
from properties.models import PROPERTIES_CATEGORIES, PROPERTIES_TYPES
from cities_light.models import City, Region
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
# from crispy_forms.bootstrap import StrictButton


class SearchForm(forms.Form):
    category = forms.ChoiceField(
        choices=PROPERTIES_CATEGORIES, widget=forms.Select(), required=False)
    city = forms.ModelChoiceField(
        queryset=Region.objects.all(), required=False)
    neighborhood = forms.ModelChoiceField(
        queryset=City.objects.all(), required=False)
    prop_type = forms.ChoiceField(
        choices=PROPERTIES_TYPES, widget=forms.Select(), required=False)
    minimum_price = forms.IntegerField(min_value=0, required=False)
    maximum_price = forms.IntegerField(min_value=0, required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'search_form'
        self.helper.form_method = 'get'
        self.helper.form_action = 'results'
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            Field('category',),
            Field('city'),
            Field('neighborhood'),
            Field('prop_type'),
            Field('minimum_price'),
            Field('maximum_price'),
        )
        self.helper.add_input(Submit('submit', 'Submit'))
