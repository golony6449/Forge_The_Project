from django.contrib import admin
from .models import Account, Context, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'passward', 'primaryLanguage')

class ContextAdmin(admin.ModelAdmin):
    list_display = ('postID','postName','contents','postDate','userID')

## https://perhapsspy.wordpress.com/2013/02/18/a-simple-way-how-to-extend-user-model-in-django-1-5/
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = '프로필'

class UserAdminExt(UserAdmin):
    # fields=('Profile.user','Profile.field','Profile.language')
    inlines = (ProfileInline,)

admin.site.register(Account)
admin.site.register(Context, ContextAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdminExt)

