from django.contrib import admin

# Register your models here.
from .models import SignUp

# Changes layout of admin page
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    class Meta:
        model = SignUp

admin.site.register(SignUp, SignUpAdmin)
