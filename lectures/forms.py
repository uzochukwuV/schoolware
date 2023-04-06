from django.forms import *
from .models import Lecturer

class LecturerForm(forms.ModelForm):
    
    class Meta:
        model = Lecturer
        fields = "__all__"
