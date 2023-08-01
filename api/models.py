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
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cv = models.FileField(upload_to='cvs/',blank=True, null=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Мужской'), ('F', 'Женский')))
    first_validation = models.BooleanField(default=False)
    second_validation = models.BooleanField(default=False)
    is_hired = models.BooleanField(default=False)

    def __str__(self):
        job_title = self.job.title if self.job else "No Job Assigned"
        return f"{self.first_name} {self.last_name} : {job_title}"