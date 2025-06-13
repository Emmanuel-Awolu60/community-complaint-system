from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at', 'status', 'upvotes')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'location')