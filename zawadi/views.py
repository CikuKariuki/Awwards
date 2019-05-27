from django.shortcuts import render

def search_results(request):
    if 'users' in request.GET and request.GET['users']:
        search_term = request.GET.get("users")
        searched_users = Profile.search_by_users(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"users":searched_users})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"users":searched_users})

class Posts(models.Model):
    images = models.ImageField(upload_to='posts/')
    caption = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.ManyToManyField(tag, blank=True)

    @classmethod
    def get_profile_posts(cls,profile):
        posts = Posts.objects.filter(profile__pk=profile)
        return posts
