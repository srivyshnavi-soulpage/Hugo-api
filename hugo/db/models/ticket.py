from django.db import models
from .users import User

class Ticket(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="hugo_users/", blank=True)
    class Meta:
       verbose_name = "Ticket"
       verbose_name_plural = "Tickets"
       db_table = "tickets"

    def __str__(self):
       return f"{self.name}"


class RequestTicket(models.Model):
       
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      # ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
      start_date = models.DateField(blank=True, null=True)
      end_date = models.DateField(blank=True, null=True)
      description = models.TextField(blank=True)
      approval = models.BooleanField(default=False)
      rejected = models.BooleanField(default=False)
      reason_for_reject = models.TextField(blank=True)
      is_half_day = models.BooleanField(default=False, blank=True)
      approval_from = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name="approval_from")
   #    notify_to = models.ManyToManyField(
   #     "self", through="RequestNotify", blank=True, symmetrical=False
   # )

      attachment = models.FileField(upload_to="hugo_users/", blank=True)

      class Meta:
         verbose_name = "Request Ticket"
         verbose_name_plural = "Request Tickets"
         db_table = "request_tickets"

      def __str__(self):
         return f"{self.ticket}-{self.user}"


class TicketAvailability(models.Model):
       
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   # ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
   availability = models.IntegerField()

   class Meta:
       verbose_name = "Ticket Availability"
       verbose_name_plural = "Ticket Availabilities"
       db_table = "ticket_availabilities"

   def __str__(self):
       return f"{self.user}-{self.ticket}"