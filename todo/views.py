from django.shortcuts import render
from task.models import Task


def home(request):
    completed = Task.objects.filter(is_completed=True).order_by('-updated_at')
    print(completed)
    not_completed = Task.objects.filter(
        is_completed=False).order_by('-updated_at')
    print(not_completed)
    return render(request, 'home.html', {'completed': completed, 'not_completed': not_completed})
