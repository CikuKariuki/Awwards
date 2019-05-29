from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Posts,Profile,Rates
from django.http import Http404
from .forms import NewPostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.models import User
from .forms import VotesForm,ReviewForm

def search_results(request):
    if 'users' in request.GET and request.GET['users']:
        search_term = request.GET.get("users")
        searched_posts = Posts.search_by_caption(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"users":searched_posts})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"users":searched_posts})

def posts(request):
    posts = Posts.objects.all()
    return render(request,'posts.html',{"posts":posts})


def post_details(request,post_id):
 
    posts = Posts.objects.get(id=post_id)
    print(posts)
    all = Rates.objects.filter(project=post_id)


    count = 0
    for i in all:
        count+=i.usability
        count+=i.design
        count+=i.content
    
    if count > 0:
        average = round(count/3,1)
    else:
        average = 0
        
    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = post_id
            rate.save()
        return redirect('post_details',post_id)
        
    else:
        form = VotesForm() 
        
    # The votes logic
    votes = Rates.objects.filter(project=post_id)
    usability = []
    design = []
    content = [] 
    
    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content) 
        
    if len(usability) > 0 or len(design)>0 or len(content)>0:
        average_usability = round(sum(usability)/len(usability),1) 
        average_design = round(sum(design)/len(design),1)
        average_content = round(sum(content)/len(content),1) 
            
        average_rating = round((average_content+average_design+average_usability)/3,1) 
    
    else:
        average_content=0.0
        average_design=0.0
        average_usability=0.0
        average_rating = 0.0
        
    '''
    To make sure that a user only votes once
    '''
    
    arr1 = []
    for use in votes:
        arr1.append(use.user_id) 
                
    auth = arr1
            
        

       
    context = {
        'posts':posts,
        'form':form,
        'usability':average_usability,
        'design':average_design,
        'content':average_content,
        'average_rating':average_rating,
        'auth':auth,
        'all':all,
        'average':average,   
    }

    return render(request,'single_post.html',context)

    


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.profile = current_user
            posts.save()
        return redirect('posts')
    else:
        form = NewPostForm()

    

    
    return render(request,'new_post.html')

@login_required(login_url='/accounts/login/') 
def profile(request, username):
    profile = User.objects.get(username=username)

    try:
        profile_details = Profile.get_by_id(profile.id)
    
    except:
        profile_details = Profile.filter_by_id(profile.id)
      

    posts = Posts.get_profile_posts(profile.id) 

    context = {
        "profile":profile,
        "profile_details":profile_details,
        "posts":posts,
    }

    return render(request,'profile.html',context)

class PostList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_posts = Posts.objects.all()
        serializers = PostSerializer(all_posts, many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = PostSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = ProfileSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostDescription(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get_post(self,pk):
#         try:
#             return Posts.objects.get(pk = pk)
#         except Posts.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format=None):
#         post = self.get_post(pk)
#         serializers = PostSerializer(post)
#         return Response(serializers.data)

# class ProfileDescription(APIView):
#     permission_classes = (IsAdminOrReadOnly,)
#     def get_profile(self, pk):
#         try:
#             return Profile.objects.get(pk = pk)
#         except Profile.DoesNotExist:
#             return Http404

#     def get(self,request,pk,format=None):
#         profile = self.get_profile(pk)
#         serializers = ProfileSerializer(profile)
#         return Response(serializers.data)