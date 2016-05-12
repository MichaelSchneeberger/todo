from django import forms

class HaveToForm(forms.Form):
	task_name = forms.CharField(label='task_name', max_length=200)
	task_text = forms.CharField(label='task_text', widget=forms.Textarea)
	start_date = forms.DateTimeField(label='start_date', input_formats='%Y%m%d %H%M%S', required=False)
	should_be_date = forms.DateTimeField(label='should_be_date', input_formats='%Y%m%d %H%M%S', required=False)
	due_date = forms.DateTimeField(label='due_date', input_formats='%Y%m%d %H%M%S', required=False)
