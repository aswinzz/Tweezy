from django.shortcuts import render
from django.http import HttpResponse
from .models import Document
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.conf import settings
from .main import singleuser

# Create your views here.
def main(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        username=str(request.POST['username'])
        if form.is_valid():
            form.save()
            details=singleuser(username)
            print(details)
            return HttpResponse("Url rank = "+str(details[0])+"\nSimilarity rank = "+str(details[1])+"\nWOT rank"+str(details[2])+"\nAdult content rank"+str(details[3])+"\nTime rank "+str(details[4])+ "Fal value = "+str(details[5]) + "type = "+str(details[6]) )
    else:
        form=DocumentForm()
    return render(request,'main.html',{
        'form' : form
    })
