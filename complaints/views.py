from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint 
from django.shortcuts import get_object_or_404
from rest_framework import generics 
from .serializers import ComplaintSerializer

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
    status_filter = request.GET.get('status', '')  # Get ?status= from URL
    if status_filter and status_filter != 'all':
        complaints = Complaint.objects.filter(status=status_filter).order_by('-created_at')
    else:
        complaints = Complaint.objects.all().order_by('-created_at')

    return render(request, 'complaints/complaint_list.html', {
        'complaints': complaints,
        'status_filter': status_filter  # Pass to template to keep dropdown selected
    })

def upvote_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.upvotes += 1
    complaint.save()
    return redirect('complaint_list')

# TO LIST ALL COMPLAINTS & CREATE NEW
class ComplaintListCreateAPIView(generics.ListCreateAPIView):
    queryset = Complaint.objects.all().order_by('-created_at')
    serializer_class = ComplaintSerializer

# TO RETRIEVE, UPDATE, DELETE SINGLE COMLAINT
class ComplaintDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complaint.object.all()
    serializer_class = ComplaintSerializer