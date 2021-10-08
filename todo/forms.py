from django import forms

class AddTask(forms.Form):
	task = forms.CharField()