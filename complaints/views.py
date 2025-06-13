from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint  # <-- Make sure this is here!

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('complaint_submitted')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/submit_complaint.html', {'form': form})

def complaint_submitted(request):
    return render(request, 'complaints/complaint_submitted.html')

def complaint_list(request):
    complaints = Complaint.objects.order_by('-created_at')
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})
