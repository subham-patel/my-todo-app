from django import forms


class TodoForm(forms.Form):
	text = forms.CharField(max_length=40,
		widget=forms.TextInput(
			attrs={'class' : 'form-control',  'placeholder' : 'Type here... (what you want to add)', 'aria-lable' : 'Todo', 'aria-describedly' : 'add-btn'}))