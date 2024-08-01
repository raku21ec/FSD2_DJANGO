from django.db import models


class BusTicket(models.Model):
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Ticket for {self.passenger_name}"