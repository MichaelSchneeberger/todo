import re

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.db.models import Q
from datetime import datetime

from .models import HaveToTask
from .forms import HaveToForm

def alltodo(request):
    todo_list = HaveToTask.objects.filter(done_date__isnull=True)
    context = {'todo_list': todo_list}
    return render(request, 'todo/alltodo.html', context)

def overview(request):
    open_todo_list = HaveToTask.objects.filter(done_date__isnull=True)
    soft_todo = open_todo_list.filter( \
        Q(start_date__lte=timezone.now()) | Q(start_date__isnull=True), \
    ).order_by('soft_due_date').first()
    hard_todo_list = open_todo_list.filter( \
        soft_due_date__lte=timezone.now(), hard_due_date__isnull=False
    )
    context = {'soft_todo': soft_todo,
               'hard_todo_list': hard_todo_list}
    return render(request, 'todo/overview.html', context)

def prostpone_date(request):
    try:
        todo_id = request.POST['todo_id']
        prospone_date = _convert_input_to_date(request.POST['prospone_date'])
        todo = HaveToTask.objects.get(pk=todo_id)
        todo.soft_due_date = prospone_date
        todo.save()
    except:
        pass
    return HttpResponseRedirect('../overview/')

def set_todo_as_done(request):
    try:
        todo_id = request.POST['todo_id']
        todo = HaveToTask.objects.get(pk=todo_id)
        todo.done_date = timezone.now()
        todo.save()
    except:
        pass
    return HttpResponseRedirect('../overview/')

def _convert_input_to_date(date_input):
    format_date_list = ['%Y%m%d', '%Y%m%d %H%M']
    format_interval_list = [r'\+(\d+)']
    current_tz = timezone.get_current_timezone()
    date_object = None
    for format in format_date_list:
        try:
            date_object = current_tz.localize(datetime.strptime(date_input, format))
            break
        except:
            pass

    for format in format_interval_list:
        try:
            interval = int(re.match(format, date_input, re.M | re.I).group(1))
            date_object = timezone.now() + timezone.timedelta(days=interval)
            break
        except:
            pass

    return date_object

def addtodo(request):
    if request.method == 'POST':
        form = HaveToForm(request.POST)
        if form.is_valid():
            have_to_task = HaveToTask(task_name=form.cleaned_data['todo_name'], \
                                      task_text=form.cleaned_data['todo_text'], \
                                      start_date=_convert_input_to_date(form.cleaned_data['start_date']), \
                                      soft_due_date=_convert_input_to_date(form.cleaned_data['soft_due_date']), \
                                      hard_due_date=_convert_input_to_date(form.cleaned_data['hard_due_date']))
            have_to_task.save()
        else:
            print('not valid')
        return HttpResponseRedirect('../overview/')
    else:
        form = HaveToForm()
        return render(request, 'todo/addtodo.html', {'form': form})
