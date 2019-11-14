from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password, is_staff,
                     is_superuser, **extra_fields):

        email = self.normalize_email(email)
        if not email:
            pass
            # raise ValueError('El email debe ser obligatorio')
        user = self.model(username=username, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True,
                                 True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    #general
    username = models.CharField(max_length=100, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField()
    #personal
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    #extras
    avatar = models.ImageField(upload_to="avatar",blank=True)
    type_user = models.IntegerField(default=0,choices=type_user_choice)

    
    



    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def get_short_name(self):
        return self.username








