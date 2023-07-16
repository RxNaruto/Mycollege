from django.shortcuts import render, redirect
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from .models import Project, UploadedFile

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_files = request.FILES.getlist('files')  # Retrieve multiple uploaded files

            for uploaded_file in uploaded_files:
                instance = UploadedFile(
                    name=form.cleaned_data['name'],
                    files=uploaded_file,
                    file_type=form.cleaned_data['file_type'],
                    tech_stack=form.cleaned_data['tech_stack'],
                    user=request.user
                )
                instance.save()

            return render(request, 'success.html')
    else:
        form = FileUploadForm()
    return render(request, 'file_upload.html', {'form': form})



def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

