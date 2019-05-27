from django.db import models

class Posts(models.Model):
    images = models.ImageField(upload_to='posts/')
    caption = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.ManyToManyField(tag, blank=True)

    @classmethod
    def get_profile_posts(cls,profile):
        posts = Posts.objects.filter(profile__pk=profile)
        return posts

    @classmethod
    def search_by_posts(cls,search_term):
        posts = cls.objects.filter(posts__icontains=search_term)
        return posts
