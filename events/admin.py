from django.contrib import admin
from .models import Service, Event, Contact


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'pillar', 'order', 'created_at')
    list_filter = ('pillar', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('order',)

    fieldsets = (
        ('Informations', {'fields': ('title', 'pillar')}),
        ('Contenu', {'fields': ('description',)}),
        ('Affichage', {'fields': ('order',)}),
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'featured', 'created_at')
    list_filter = ('featured', 'date', 'created_at')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'date'

    fieldsets = (
        ('Informations', {'fields': ('title', 'date', 'location')}),
        ('Contenu', {'fields': ('description', 'image')}),
        ('Affichage', {'fields': ('featured',)}),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
