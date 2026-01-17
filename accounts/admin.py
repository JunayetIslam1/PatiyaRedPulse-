from django.contrib import admin
from .models import Donor


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'blood_group', 'mobile_number', 'district', 'upazila', 
                   'last_donation_date', 'eligibility_status', 'availability_status', 'is_active']
    list_filter = ['blood_group', 'availability_status', 'is_active', 'district']
    search_fields = ['full_name', 'mobile_number', 'district', 'upazila']
    list_editable = ['availability_status', 'is_active']
    
    def eligibility_status(self, obj):
        return obj.eligibility_status
    eligibility_status.short_description = 'Eligibility Status'
    
    readonly_fields = ['registration_date', 'eligibility_status']