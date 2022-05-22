from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Movie
from .forms import ContactForm, MovieForm, NameForm
from django.contrib import messages
#add email module
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST, request.FILES)
        if movie_form.is_valid():
            movie_form.save()
            messages.success(request, "You Movie was successfully ADDED!")
        else:
            messages.error(request, "Error saving form")

        return redirect("form_app:index")

    movie_form = MovieForm()
    movies = Movie.objects.all()

    return render(
                    request=request, 
                    template_name='form_app/index.html', 
                    context={
                        'movie_form': movie_form, 
                        'movies': movies
                        })



def get_name(request):
    # If this is a POST Request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        #Check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'form_app/name_list.html', {'form': form})

def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message =form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['maarufburad1231@gmail.com']
            if cc_myself:
                recipients.append[sender]

            send_mail(subject, message, sender, recipients)

            return HttpResponse('<h1>Email Sends</h1>')

    else:
        form = ContactForm()

    return render(request, 'form_app/contact_me.html', {'form': form})



def author_list(request):
    if request.method == "POST":
        pass

    else:
        pass



def book_list(request):
    if request.method == "POST":
        pass
    
