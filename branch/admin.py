from django.contrib import admin

from . models import Branch


admin.site.site_header = 'FINANCIAL MANAGEMENT SYSTEM'
admin.site.site_title = 'AVIID FINANCE'


class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'opening_date', 'country',
                    'county', 'city', 'phone_number', 'is_active')
    list_display_links = ('id',)
    list_editable = ('name', 'country', 'county', 'city',
                     'phone_number', 'is_active',)
    search_fields = ('name', 'county', 'is_active')


admin.site.register(Branch, BranchAdmin)
