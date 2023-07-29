from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        (1, 'Админ'),
        (2, 'Первый Админ'),
        (3, 'Второй Админ'),
        (4, 'Главный Админ'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES, default=1)


class Job(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    cv = models.FileField(upload_to='cvs/')
    gender = models.CharField(max_length=1, choices=(('M', 'Мужской'), ('F', 'Женский')))
    is_hired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.job.title}"