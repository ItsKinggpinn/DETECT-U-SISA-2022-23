from django.shortcuts import render
from .models import Contact
# Create your views here.


def home2(request):
    if request.method == "POST":
        name = request.POST.get('name', 'default')
        email = request.POST.get('email', 'default')
        message = request.POST.get('message', 'default')
        o = Contact(name=name, email=email, message=message)
        o.save()
        return render(request, 'Home2.html')
    return render(request, 'Home2.html')
