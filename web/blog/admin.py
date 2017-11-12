from django.contrib import admin
from .models import Account, Context

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'passward', 'primaryLanguage')

class ContextAdmin(admin.ModelAdmin):
    list_display = ('postID','contents','postDate','userID')

admin.site.register(Account)
admin.site.register(Context)

