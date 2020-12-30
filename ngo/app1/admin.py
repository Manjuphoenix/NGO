from django.contrib import admin
from .models import *

# Register your models here.
'''@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'country']'''


'''@admin.register(cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ['name', 'goal', 'raised', 'img', ]'''

admin.site.register(Volunteer)
admin.site.register(cause)
admin.site.register(Contributors)
admin.site.register(Donation)
admin.site.register(Events)
admin.site.register(Adopt)
admin.site.register(Index)