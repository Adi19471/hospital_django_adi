from django.contrib import admin

# Register your models here.

from .models import ClaimStatus,Claim

admin.site.register(ClaimStatus)
admin.site.register(Claim)

