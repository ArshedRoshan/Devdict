from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50,unique=True)
    email           = models.EmailField(max_length=100)
    phone_number    = models.IntegerField(null = True,blank=True)
    Account_type    = models.CharField(max_length=50)
    company_name    = models.CharField(max_length=200,blank=True)
    Describe_company = models.CharField(max_length=200,blank=True)
    hiring_for = models.CharField(max_length=100,blank=True)
    follow = models.IntegerField(default=0)
    follower = models.IntegerField(default=0)
    is_verfied = models.BooleanField(default=False)
    is_follow = models.BooleanField(default = False)
    is_follower = models.BooleanField(default = False)
    is_block = models.BooleanField(default=True)
    
    

    # required
    date_joined     = models.DateTimeField(auto_now_add=True,null=True)
    last_login      = models.DateTimeField(auto_now_add=True,null=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_superadmin    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    
    def get_username(self):
        return self.username
    
    def get_company_name(self):
        return self.company_name

class follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    
    # def follow(self, user):
    #     self.followee.add(user)

    # def unfollow(self, user):
    #     self.followee.remove(user)
        
    # def is_following(self, user):
    #     return self.followee.filter(pk=user.pk).exists()
    
    
class profile(models.Model):
    user= models.ForeignKey(User,related_name='pro',on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/',blank=True)
    bio = models.CharField(max_length=500,blank=True)
    

class Application(models.Model):
    user = models.ForeignKey(User,related_name='jobs',on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Phone_number = models.IntegerField()
    resume = models.FileField(upload_to='static/',verbose_name='resume')
    company_name = models.ForeignKey(User,related_name='com',on_delete=models.CASCADE)
    processing = models.CharField(max_length=20,default=False)
    Accept = models.CharField(max_length=20,default=False)
    Decline = models.CharField(max_length=25,default=False)