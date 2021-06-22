from django.contrib import admin
from myapp.models import form,maid_registerm,user_registerm

# Register your models here.
admin.site.register(form)
admin.site.register(maid_registerm)
admin.site.register(user_registerm)