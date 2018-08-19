from django.contrib import admin
from accounts.models import alllocations,allcoordinates,helicopdrones

# Register your models here.

admin.site.register(alllocations)
admin.site.register(allcoordinates)
admin.site.register(helicopdrones)
