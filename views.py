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
    todo_list = HaveToTask.objects.filter( \
        Q(start_date__lte=timezone.now()) | \
        Q(start_date__isnull=True), \
        Q(done_date__isnull=True))
    context = {'todo_list': todo_list}
    return render(request, 'todo/alltodo.html', context)

def addtodo(request):
    if request.method == 'POST':
        form = HaveToForm(request.POST)
        if form.is_valid():

            def convert_input_to_date(date_input):
                format_list = ['%Y%m%d', '%Y%m%d %H%M']
                current_tz = timezone.get_current_timezone()
                date_object = None
                for format in format_list:
                    try:
                        date_object = current_tz.localize(datetime.strptime(date_input, format))
                        break
                    except:
                        pass
                return date_object

            have_to_task = HaveToTask(task_name=form.cleaned_data['todo_name'], \
                                      task_text=form.cleaned_data['todo_text'], \
                                      start_date=convert_input_to_date(form.cleaned_data['start_date']), \
                                      soft_due_date=convert_input_to_date(form.cleaned_data['soft_due_date']), \
                                      hard_due_date=convert_input_to_date(form.cleaned_data['hard_due_date']))
            have_to_task.save()
        else:
            print('not valid')
        return HttpResponseRedirect('../overview/')
    else:
        form = HaveToForm()
        return render(request, 'todo/addtodo.html', {'form': form})
