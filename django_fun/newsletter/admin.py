from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

# Changes layout of admin page
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "full_name", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)
