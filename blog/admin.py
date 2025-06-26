from django.contrib import admin

# Register your models here.
from .models import Box,Description,BoxImage,ContactMessage

admin.site.register(Description)
class BoxImageInline(admin.TabularInline):
    model = BoxImage
    extra = 1

class BoxAdmin(admin.ModelAdmin):
    inlines = [BoxImageInline]

admin.site.register(Box, BoxAdmin)  
admin.site.register(ContactMessage)  



