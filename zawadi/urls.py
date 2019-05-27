from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.posts,name='posts'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^new/',views.new_post,name='new_post'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)