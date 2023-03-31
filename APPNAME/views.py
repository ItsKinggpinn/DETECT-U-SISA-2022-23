import cv2 as c
from django.shortcuts import render

from .models import Image
# Create your views here.

def home(request):
    if request.method == "POST":
        title=request.POST.get('title','default')
        photo=request.FILES.get('photo','default')

        o=Image(title=title,photo=photo)
        o.save()
        face_cascade = c.CascadeClassifier('media/myimage/haarcascade_frontalface_default.xml')
        img = c.imread(f'media/myimage/{photo}')
        gray = c.cvtColor(img, c.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            c.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        c.imwrite(f'static/{photo}',img)
        # print(img)
        p={
            'img':photo
        }
        return render(request,'home.html',p)
    return render(request,'home.html')



def about(request):
    return render(request,'About.html')
    
def team(request):
    return render(request,'Team.html')

def detect(request):
    if request.method == "POST":
        title=request.POST.get('title','default')
        photo=request.FILES.get('photo','default')

        o=Image(title=title,photo=photo)
        o.save()
        face_cascade = c.CascadeClassifier('media/myimage/haarcascade_frontalface_default.xml')
        img = c.imread(f'media/myimage/{photo}')
        gray = c.cvtColor(img, c.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            c.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        c.imwrite(f'static/{photo}',img)
        # print(img)
        p={'img':photo}
        return render(request,"Detect.html",p)
    return render(request,"Detect.html")