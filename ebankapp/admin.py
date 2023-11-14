from django.contrib import admin

from ebankapp.models import Registration,District,Branch

# Register your models here.
admin.site.register(Registration)
admin.site.register(District)
admin.site.register(Branch)