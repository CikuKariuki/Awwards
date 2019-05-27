from django.contrib import admin
from .models import Profile,Posts

class PostsAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Profile)
admin.site.register(Posts)
