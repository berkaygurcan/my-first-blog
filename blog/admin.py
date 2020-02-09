from django.contrib import admin
from .models import Post

# Register your models here.


admin.site.register(Post) # Admin sayfasında modelimizi görünür kılabilmek için, modeli admin.site.register(Post) ile kaydetmemiz gerekiyor.

