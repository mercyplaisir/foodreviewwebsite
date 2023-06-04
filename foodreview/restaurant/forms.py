from django import forms
from .models import Restaurant,Restaurant_address

class Restaurant_creation_form(forms.ModelForm):
    class Meta:
        model =  Restaurant
        fields = ['name']
    
    def manual_save(self,creator,address):
        name = self.cleaned_data['name']
        rest = Restaurant(name=name,
                          creator = creator,
                          address=address)
        return rest.save()

class Address_input_form(forms.ModelForm):
    class Meta:
        model = Restaurant_address
        fields = '__all__'