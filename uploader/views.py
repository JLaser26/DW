from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UploadedFile

def home(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'uploader/home.html', {'files': files})

# Helper function: only allow users in "Uploader" group
def is_uploader(user):
    return user.is_authenticated and user.groups.filter(name='uploader').exists()

@user_passes_test(is_uploader, login_url='permission_denied')
def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        UploadedFile.objects.create(title=title, description=description, file=file)
        messages.success(request, '✅ File uploaded successfully!')
        return redirect('home')
    return render(request, 'uploader/upload.html')

def permission_denied(request):
    return render(request, 'uploader/permission_denied.html')
