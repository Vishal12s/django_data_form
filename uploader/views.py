import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Upload
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('generate_report')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})

def generate_report(request):
    last_upload = Upload.objects.last()
    if not last_upload:
        return HttpResponse("No file uploaded.")

    file_path = last_upload.file.path
    df = pd.read_excel(file_path)

    report = df.groupby(['Cust State', 'DPD']).size().reset_index(name='Count')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    report.to_csv(path_or_buf=response, index=False)

    return response

# Create your views here.
