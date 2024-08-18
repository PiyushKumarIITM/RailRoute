from django.db import models

class Day(models.Model):
    name = models.CharField(max_length=9, choices=[
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ],
    default='Monday'
    )

    def __str__(self):
        return self.name

class Train(models.Model):
    train_name = models.CharField(max_length=255)
    start = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    starting_time = models.TimeField(null=True, blank=True)
    reaching_time = models.TimeField(null=True, blank=True)
    days = models.ManyToManyField(Day)

    def __str__(self):
        return self.train_name

    def get_days(self):
        return ", ".join(day.name for day in self.days.all())
    get_days.short_description = 'Days'
