from django.contrib import admin

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'location', 'is_published', 'listing_date')
    list_display_links = ('id', 'title')
    list_filter = ('is_published', 'location')
    search_fields = ('title', 'location', 'price')
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)


# Register your models here.
