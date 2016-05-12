from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q

from .models import HaveToTask
from .forms import HaveToForm

def overview(request):
    todo_list = HaveToTask.objects.filter( \
		Q(start_date__lte = timezone.now()) | \
                Q(start_date__isnull = True))
    context = {'todo_list': todo_list}
    return render(request, 'todo/overview.html', context)
		
def addtodo(request):
    if request.method == 'POST':
        form = HaveToForm(request.POST)
        if form.is_valid():
            have_to_task = HaveToTask(task_name=form.cleaned_data['task_name'], \
                                      task_text=form.cleaned_data['task_text'], \
                                      start_date=form.cleaned_data['start_date'], \
                                      should_be_date=form.cleaned_data['should_be_date'], \
                                      due_date=form.cleaned_data['due_date'])
            have_to_task.save()
        else:
            print('not valid')
        return HttpResponseRedirect('../overview/')
    else:
        form = HaveToForm()
        return render(request, 'todo/addtodo.html', {'form': form})
