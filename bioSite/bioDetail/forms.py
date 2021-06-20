from django import forms
from .models import UserData, UserFingerprint

class UserForm(forms.ModelForm):
	class Meta:
		model = UserData
		labels = {
			'phone': 'Phone Number',
			'photo': 'Profile Image',
			'address': 'Address',
		}
		# widgets = {
  #           'address': forms.Textarea(attrs={'class': 'form-control', 'cols':10}),
  #           'gender': forms.RadioSelect(attrs={'class': 'form-check form-check-inline'}),
  #           'name': forms.TextInput(attrs={'class': 'form-control'}),
  #           'email': forms.EmailInput(attrs={'class': 'form-control'}),
  #           'occupation': forms.TextInput(attrs={'class': 'form-control'}),
  #           'organisation': forms.TextInput(attrs={'class': 'form-control'}),
  #           'phone': forms.NumberInput(attrs={'class': 'form-control'}),
  #           'photo': forms.FileInput(attrs={'class': 'form-control'}),
  #       }
		fields = ["name", "email", "gender", "phone", "address", "occupation", "organisation", "photo"]
		

class FingerForm(forms.Form):
	f_img = forms.ImageField(label='FingerPrint Image')
