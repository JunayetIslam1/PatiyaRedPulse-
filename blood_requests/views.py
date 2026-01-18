from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BloodRequestForm
from .models import BloodRequest
from accounts.models import Donor


def home(request):
    total_donors = Donor.objects.filter(is_active=True, availability_status='Available').count()
    total_requests = BloodRequest.objects.filter(is_active=True).count()
    emergency_requests = BloodRequest.objects.filter(is_active=True, emergency_level='Emergency').count()
    
    context = {
        'total_donors': total_donors,
        'total_requests': total_requests,
        'emergency_requests': emergency_requests,
        'title': 'Patiya RedPulse - Blood Donor Directory'
    }
    return render(request, 'blood_requests/home.html', context)


def submit_blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.is_active = True
            blood_request.save()
            
            messages.success(request, 'Blood request submitted successfully! We will review it shortly.')
            return redirect('blood_requests_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = BloodRequestForm()
    
    context = {
        'form': form,
        'title': 'Submit Blood Request'
    }
    return render(request, 'blood_requests/submit_request.html', context)


def blood_requests_list(request):
    requests = BloodRequest.objects.filter(is_active=True).order_by('-request_date')
    
    context = {
        'requests': requests,
        'title': 'Blood Requests'
    }
    return render(request, 'blood_requests/requests_list.html', context)