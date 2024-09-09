from django.contrib import admin

# Register your models here.
from .models import Drug

class DrugAdmin(admin.ModelAdmin):
    list_display = ('drug_name', 'category', 'expiry_date', 'stock')
    search_fields = ('drug_name', 'manufacturer')

admin.site.register(Drug, DrugAdmin)