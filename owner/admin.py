from django.contrib import admin
from .models import Owner

# Register your model here.

#admin.site.register(Owner)

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre', "pais", "edad")
    list_filter = ("edad", "pais")
    search_fields = ("nombre","pais")
    #fields = ("nombre", "edad")