from django.db import models
from tinymce import models as tinymce_models
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.templatetags.static import static



User = get_user_model()

def default_profile_picture():
    return static('admin/author1.jpg')

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='admin/author1.jpg')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    overview = models.TextField()
    thumbnail = models.ImageField()
    content = tinymce_models.HTMLField() 
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })
    
    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
