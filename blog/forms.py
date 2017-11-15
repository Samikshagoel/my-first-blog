from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)


class SignUpForm(UserCreationForm):
	birth_date = forms.DateField(help_text='Required. Format=YYYY-MM-DD')
	#bio = forms.TextField(max_length = 30)
	location = forms.CharField(max_length = 30)
	class Meta:
		model = User
		fields = ('username', 'birth_date', 'location', 'password1', 'password2',)