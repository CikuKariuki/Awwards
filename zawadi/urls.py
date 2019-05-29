from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.posts,name='posts'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^new/',views.new_post,name='new_post'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^api/post/$', views.PostList.as_view(),name='posts_api'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profiles_api'),
    url(r'^posts/(\d+)',views.post_details,name='Voteposts'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)