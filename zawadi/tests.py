from django.test import TestCase
from .models import Profile,Posts
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='test',email='test@com',password='hjhj')

        self.wanjiku = Profile(first_name = 'Wanjiku',last_name='Kariuki',email='sheekokariuki@gmail.com',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.wanjiku,Profile))

    def test_save(self):
        self.wanjiku.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0) 

    
 

class PostsTestClass(TestCase):
    def setUp(self):
        self.wanjiku = Profile(first_name = 'Wanjiku',last_name='Kariuki',username='ciku_k',email='sheekokariuki@gmail.com')
        self.wanjiku.save_profile()

        self.new_post =Posts(caption="testing testing 1,2",profile=self.wanjiku)
        self.new_post.save()

    def tearDown(self):
        Profile.objects.all().delete()
        tag.objects.all().delete()
        Posts.objects.all().delete()    

    def test_posts(self):
        posts = Posts.posts()
        self.assertTrue(len(posts)>0)