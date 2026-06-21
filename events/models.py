from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50, default='Hackathon')
    date = models.DateField()
    location = models.CharField(max_length=150)
    description = models.TextField()
    total_slots = models.IntegerField(default=50)

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    college_name = models.CharField(max_length=150)
    department = models.CharField(max_length=100)
    current_year = models.CharField(max_length=20)
     
    def __str__(self):
        return self.name