from django.db import models

class HaveToTask(models.Model):
	task_name = models.CharField(max_length=200)
	task_text = models.TextField(blank=True, null=True)
	start_date = models.DateTimeField(blank=True, null=True)
	soft_due_date = models.DateTimeField(blank=True, null=True)
	hard_due_date = models.DateTimeField(blank=True, null=True)
	done_date = models.DateTimeField(blank=True, null=True)
	def __str__(self):
	    return self.task_name
