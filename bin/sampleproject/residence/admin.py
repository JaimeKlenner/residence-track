from django.contrib import admin

# Register your models here.
from .models import Residence

admin.site.register(Residence)

from .models import	UserAntenna

admin.site.register(UserAntenna)