from django.shortcuts import render
from MyFileUploadApp.models import Document
from MyFileUploadApp.forms import DocumentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def uploadView(request):
    if request.method == "POST":
        img=DocumentForm(request.POST,request.FILES)
        if img.is_valid():
            img.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        img = DocumentForm()
        images=Document.objects.all().order_by('-uploaded_at')
        return render (request,'Core/upload.html',{'form':img, 'images':images})
