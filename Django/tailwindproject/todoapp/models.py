from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(null = True, blank = True)
    status = models.CharField(max_length=100, default = 'Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


