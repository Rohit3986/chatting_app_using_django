
from dataclasses import field

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
class Student(AuthenticationForm):
    class Meta:
        model=User
        fields=['first_name','email','last_name']
        label={"first_name":"your_name"}
