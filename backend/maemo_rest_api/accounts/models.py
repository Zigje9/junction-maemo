from django.db import models
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, name, phone, password=None):
        if not name:
            raise ValueError('Users must have a name')

        user = self.model(
            name=name,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone, password):
        user = self.create_user(
            name=name,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        verbose_name='name',
        max_length=12,
        unique=True,
    )
    
    phone = models.CharField(
        verbose_name='phone',
        max_length=12,
        unique=True,
    )

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['phone',]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin




class Profile(models.Model):

    NONE = 'none'
    CHALLENGED = 'challenged'
    INFANT_COMPANION = 'infant_companion'
    PREGNANT = 'pregnant'
    CHILD = 'child'

    FAMILY = 'family'
    SIBLING = 'sibling'
    RELATIVE = 'relative'
    FRIEND = 'friend'
    LOVER = 'lover'
    ETC = 'etc'

    USER_TYPES = [
        (NONE, 'NONE'),
        (CHALLENGED, 'CHALLENGED'),
        (PREGNANT, 'PREGNANT'),
        (INFANT_COMPANION, 'INFANT_COMPANION'),
        (CHILD, 'CHILD'),
    ]

    PROTECTOR_TYPES = [
        (NONE, 'NONE'),
        (FAMILY, 'FAMILY'),
        (SIBLING, 'SIBLING'),
        (RELATIVE, 'RELATIVE'),
        (FRIEND, 'FRIEND'),
        (LOVER, 'LOVER'),
        (ETC, 'ETC')
    ]

    name = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='User'
    )

    phone = models.CharField(max_length=12, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default=NONE, blank=True, help_text='유저 타입')
    challenged_type = models.CharField(max_length=50, blank=True)
    protector_type = models.CharField(max_length=20, choices=PROTECTOR_TYPES, default=NONE, blank=True, help_text='보호자 타입')
    protector_phone = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return str(self.name)