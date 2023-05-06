from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,firstname,lastname,username,email,password=None):
        if not email:
            raise ValueError("Please provide an email address")
        if not username:
            raise ValueError("Please provide a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, firstname,lastname,username,email,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return 
    
class User(AbstractBaseUser):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True



class Profile(models.Model):
    profile_pic = models.ImageField(null=True,blank=True, default='',upload_to='users/profile_picture')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.user

class Code(models.Model):
    profile = models.ForeignKey(Profile, related_name="profile", on_delete=models.DO_NOTHING)
    question = models.TextField(max_length=5000)
    code_answer = models.TextField(max_length=5000)
    language = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.question