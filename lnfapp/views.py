from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import profile

# Create your views here.
def home(request):
    all=profile.objects.all()
    return render(request, 'home.html', {'uploads': all})
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs = FileSystemStorage()
        filename= fs.save(myfile.name, myfile)
        url='www.google.com'
        url = fs.url(filename)
        new_profile = profile(
            name=request.POST['name'],
            phone=request.POST['phone'],
            item=request.POST['item'],
            category=request.POST['category'],
            description=request.POST['description'],
            location=request.POST['location'],
            image = url
        )
        new_profile.save()
        return render(request, 'submitdone.html')
def lostform(request):
    return render(request, 'lostform.html')
def seepost(request):
    return render(request, 'seepost.html')
def lostposts(request):
    all=profile.objects.filter(category="LOST")
    return render(request, 'lostposts.html', {'uploads': all})
def foundposts(request):
    all=profile.objects.filter(category="FOUND")
    return render(request, 'foundposts.html', {'uploads': all})