from django import forms
from .models import (Movie, Blog, Author, Book)
from django.core.exceptions import NON_FIELD_ERRORS
# Create your owm forms her

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('movie_title', 'release_year', 'movie_poster') #'__all__'


# This is an example using forms.Form
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name',max_length=100)

# Another Examples
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    subject.widget.attrs.update({'class': 'text-danger', 'style': 'background-color:red'})

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

        error_messages = {
            NON_FIELD_ERRORS :{'unique_together': "%(model_name)s's %(field_labels)s are not unique.",} 
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']
