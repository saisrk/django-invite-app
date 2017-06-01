from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import EmailInvitation

def index(request):
    invitations = EmailInvitation.objects.all()
    return render(request, 'index.html', {'invitations':invitations})
