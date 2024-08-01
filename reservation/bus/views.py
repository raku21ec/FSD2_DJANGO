from django.shortcuts import render, HttpResponse

# Create your views here.
def layout(request):
    return render(request, 'layout.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import BusTicketForm
from .models import BusTicket

def book_ticket(request):
    if request.method == 'POST':
        form = BusTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            send_ticket_email(ticket)
            return redirect('success')
    else:
        form = BusTicketForm()
    return render(request, 'book_ticket.html', {'form': form})

def send_ticket_email(ticket):
    subject = 'Your Bus Ticket'
    message = render_to_string('ticket_email.html', {'ticket': ticket})
    email_text = strip_tags(message)
    email = EmailMultiAlternatives(subject, email_text, to=[ticket.email])
    email.attach_alternative(message,"text/html")
    email.send()

def success(request):
    return render(request, 'success.html')


#LOGIN/SIGNUP

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('layout')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('layout')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





