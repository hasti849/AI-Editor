from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Collection, Prompt, SavedPrompt, UserSettings

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'gender', 'is_onboarded', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('gender', 'is_onboarded')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Collection)
admin.site.register(Prompt)
admin.site.register(SavedPrompt)
admin.site.register(UserSettings)
