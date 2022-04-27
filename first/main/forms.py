from timeit import repeat
from turtle import width
from .models import Posts, Registration, Singers
from django import forms 
from django.forms import ModelForm, PasswordInput, TextInput, Textarea

class SingersForm(ModelForm):
     class Meta:
        model = Singers
        fields = ['song_name', 'about']
        widgets ={
            "song_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Әншінің аты'
        }),
            "about": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Әнші туралы'
            })
      }

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Registration 
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'name':forms.TextInput(attrs={'class':'form-input'}),
            'surname':forms.TextInput(attrs={'class':'form-input'}),
             'email':forms.EmailInput(attrs={'class':'form-input'}),
             'password':forms.PasswordInput(attrs={'class':'form-input'}),
             'repeat': forms.PasswordInput(attrs={'class':'form-input'}),
             'requement':forms.NumberInput(attrs={'class':'form-input'}),
             'slug':forms.TextInput(attrs={'class':'form-input'})
        }
        
