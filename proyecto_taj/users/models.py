from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Role(models.Model):
    name = models.CharField(max_length=20, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class User(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('worker', 'Worker'),
        ('consumer', 'Consumer'),
        ('staff', 'Staff'),
    ]

    #roles = models.ManyToManyField(Role, related_name='user_roles', verbose_name='User Roles')
    roles = models.ManyToManyField(Role, related_name='user_roles', verbose_name='User Roles', blank=True)
    phoneNumber = models.CharField(max_length=10, null=False)
    calGralConsumer = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    calGralWorker = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    ife = models.TextField(null=True)
    criminalRecord = models.TextField(null=True)
    birthCertificate = models.TextField(null=True)
    driverLicence = models.TextField(null=True)
    curp = models.TextField(null=True)
    photo = models.TextField(null=True)
    active = models.BooleanField(default=True, verbose_name='Is Active')
    cv = models.TextField(null=True)
    knowledgeProof = models.TextField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )


class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"
