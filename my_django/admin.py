from django.contrib import admin

# Register your models here.

from my_django.models import Host,HostGroup,UserProfile,IDC

admin.site.register(HostGroup)
admin.site.register(Host)
admin.site.register(UserProfile)
admin.site.register(IDC)
