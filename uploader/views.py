from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UploadedFile
from .models import UploadedFile
from .forms import UploadFileForm

def home(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')
    return render(request, 'uploader/home.html', {'files': files})

# Helper function: only allow users in "Uploader" group
def is_uploader(user):
    return user.is_authenticated and user.groups.filter(name='uploader').exists()


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Uploader').exists(), login_url='/permission-denied/')
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'uploader/upload.html', {'form': form})

def permission_denied(request):
    return render(request, 'uploader/permission_denied.html')
