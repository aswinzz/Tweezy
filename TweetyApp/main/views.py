from django.shortcuts import render
from django.http import HttpResponse
from .models import Document
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from django.conf import settings
# Create your views here.
def main(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
    else:
        form=DocumentForm()
    return render(request,'main.html',{
        'form' : form
    })
