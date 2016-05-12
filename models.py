from django.db import models

class HaveToTask(models.Model):
	task_name = models.CharField(max_length=200)
	task_text = models.TextField()
	start_date = models.DateTimeField(blank=True, null=True)
	should_be_date = models.DateTimeField(blank=True, null=True)
	due_date = models.DateTimeField(blank=True, null=True)
	def __str__(self):
	    return self.task_name
