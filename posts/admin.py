from django.contrib import admin
from .models import Author, Category, Post, Comment
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
