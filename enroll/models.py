
# coding: utf-8
from telnetlib import STATUS

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.send_email import send_notification
from master.models import Master, Category

User = get_user_model()
TIMESLOT_LIST = (
        (9, '09:00 – 10:00'),
        (10, '10:00 – 11:00'),
        (11, '11:00 – 12:00'),
        (12, '12:00 – 13:00'),
        (13, '13:00 – 14:00'),
        (14, '14:00 – 15:00'),
        (15, '15:00 – 16:00'),
        (16, '16:00 – 17:00'),
        (17, '17:00 – 18:00'),
    )


class Enroll(models.Model):
    Pn = 'Понедельник',
    Vt = 'Вторник',
    Sr = 'Среда',
    Cht = 'Четверг',
    Pt = 'Пятница'
    CHOICES = [
        ('Pn', 'Понедельник'),
        ('Vt', 'Вторник'),
        ('Sr', 'Среда'),
        ('Cht', 'Четверг'),
        ('Pt', 'Пятница'),
    ]
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    owner = models.ForeignKey(User, related_name='master', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='master')
    # location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    time = models.CharField(max_length=300, choices=TIMESLOT_LIST)
    schedule = models.CharField(max_length=300, choices=CHOICES)

    class Meta:

        unique_together = ('master', 'time', 'schedule')

        ordering = ('created_at',)

    def __str__(self):
        return f'{self.owner} - {self.first_name}-{self.last_name} {self.time} {self.schedule}'

@receiver(post_save, sender=Enroll)
def order_post_save(sender, instance, *args, **kwargs):
    send_notification(instance.owner, instance.id, instance.master, instance.schedule, instance.time,)