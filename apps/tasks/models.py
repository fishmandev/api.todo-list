from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    class Status(models.IntegerChoices):
        BACKLOG = 1, _('Backlog')
        IN_PROGRESS = 2, _('In progress')
        DONE = 3, _('Done')

    name = models.CharField(max_length=256)
    status = models.SmallIntegerField(default=Status.BACKLOG, choices=Status.choices)
    due_date = models.DateField(null=True)

    class Meta:
        db_table = "task"
