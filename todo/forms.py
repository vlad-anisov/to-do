from django.forms import ModelForm
from .models import Task

class TaskFrom(ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'text',)