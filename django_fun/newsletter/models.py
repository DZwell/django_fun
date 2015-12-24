from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=200, blank=True, null=True)
    # blank: refers to form field, False makes it required
    # null: refers to inside database
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # auto_now_add: when model is created
    # auto_now: when model is saved
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
