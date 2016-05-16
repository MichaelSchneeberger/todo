from django import forms

class HaveToForm(forms.Form):
	todo_name = forms.CharField(label='todo_name', max_length=200)
	todo_text = forms.CharField(label='todo_text', widget=forms.Textarea)
	start_date = forms.CharField(label='start_date', max_length=200, required=False)
	soft_due_date = forms.CharField(label='soft_due_date', max_length=200, required=False)
	hard_due_date = forms.CharField(label='hard_due_date', max_length=200, required=False)
