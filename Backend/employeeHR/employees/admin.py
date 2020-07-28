from django.contrib import admin

# Register your models here.
from .models import Admin,Login,userregister,deliveryboyregister
admin.site.register(Admin)
admin.site.register(Login)

admin.site.register(userregister)
admin.site.register(deliveryboyregister)

