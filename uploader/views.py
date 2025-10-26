from django.shortcuts import render, redirect
from .models import UploadedFile
from django.core.files.storage import FileSystemStorage

def home(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'uploader/home.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        UploadedFile.objects.create(title=title, description=description, file=file)
        return redirect('home')
    return render(request, 'uploader/upload.html')
