from django.contrib import admin
from .models import UserData, UserFingerprint

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
				("ID", {"fields": ['id']}),
				("User Name", {"fields": ['name']}),
				("Email", {"fields": ['email']}),
				("Phone Number", {"fields": ['phone']}),
				("Gender", {"fields": ['gender']}),
				("Address", {"fields": ['address']}),
				("Occupation w/ Company", {"fields": ['occupation', 'organisation']}),
				("Photo", {"fields": ['photo']}),
				("Added Date", {"fields": ['date_pub']}),
	]
	readonly_fields = ('id',)

admin.site.register(UserData, UserAdmin)
# admin.site.register(UserFingerprint)