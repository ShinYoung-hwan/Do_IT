from django.contrib import admin

from .models import DOITLIST
# Register your models here.
class DOITLISTAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(DOITLIST, DOITLISTAdmin)