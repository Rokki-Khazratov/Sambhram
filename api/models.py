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
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_custom_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_custom_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Job(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()

    def __str__(self):
        return self.title


class Application(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    cv = models.FileField(upload_to='cvs/',blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Мужской'), ('F', 'Женский')))
    is_hired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"