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

def posts(request):
    posts = Posts.objects.all()
    return render(request,'posts.html',{"posts":posts})

