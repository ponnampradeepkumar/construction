from django.contrib import admin
from .models import *

# Customize the admin interface for WorkProgress model
class WorkProgressAdmin(admin.ModelAdmin):
    list_display = ('sno','name_of_site','location', 'name_of_the_employee', 'phone_number', 'to_day_expensives', 'created_at')
    search_fields = ('name_of_the_employee', 'sno', 'phone_number')
    ordering = ('-created_at',)  # Order by creation date in descending order

    # Optional: Add inline editing for related models if needed (for example if you have a related model)
    # inlines = [SomeInlineModelAdmin]

# Register the model with the customized admin
admin.site.register(WorkProgress, WorkProgressAdmin)




from django.contrib import admin
from .models import Employee

admin.site.register(Employee)






@admin.register(contract_deal)
class ContactDealAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'contract_deal', 'location', 'created_at')
    search_fields = ('name', 'phone_number', 'contract_deal', 'location')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    # Optionally, you can add form layout customizations and fieldsets if needed
    fieldsets = (
        (None, {
            'fields': ('name', 'phone_number', 'contract_deal', 'location', 'description')
        }),
    )






