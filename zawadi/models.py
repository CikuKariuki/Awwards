from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.decorators import login_required

class Posts(models.Model):
    images = models.ImageField(upload_to='posts/')
    caption = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def get_profile_posts(cls,profile):
        posts = Posts.objects.filter(profile__pk=profile)
        return posts

    @classmethod
    def search_by_caption(cls,search_term):
        posts = cls.objects.filter(caption__icontains=search_term)
        return posts


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profiles/',default='default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=50)
    bio = models.TextField()
    phone = models.CharField(max_length=15, blank=True)

    class Meta:
        ordering = ['first_name']
        

    def save_profile(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
