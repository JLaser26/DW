from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UploadedFile

def home(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'uploader/home.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        UploadedFile.objects.create(title=title, description=description, file=file)
        messages.success(request, '✅ File uploaded successfully!')
        return redirect('home')
    return render(request, 'uploader/upload.html')
