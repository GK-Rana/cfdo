from django import forms


class AddCompany(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput( ))
	contact = forms.CharField(required=True, widget=forms.TextInput( ))
	ad1 = forms.CharField(required=True, widget=forms.TextInput( ))
	ad2 = forms.CharField(required=True, widget=forms.TextInput( ))
	city = forms.CharField(required=True, widget=forms.TextInput( ))
	properties = forms.CharField(required=True, widget=forms.TextInput( ))
 