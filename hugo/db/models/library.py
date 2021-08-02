from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

# from ..mixins import TimeAuditModel


class Event(models.Model):

    name = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)

    description = models.TextField(blank=True)

    image = models.FileField(
       upload_to="hugo_users/",
       blank=True
   )

    class Meta:
       verbose_name = "Event"
       verbose_name_plural = "Events"
       db_table = "events"

    def __str__(self):
       return self.name


class Holiday(models.Model):
   name = models.CharField(max_length=255)
   date = models.DateField(blank=True, null=True)
   description = models.TextField(blank=True)

   class Meta:
       verbose_name = "Holiday"
       verbose_name_plural = "Holidays"
       db_table = "holidays"
       unique_together = ("name", "date")

   def __str__(self):
       return self.name