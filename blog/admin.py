from django.contrib import admin
from .models import Post , Comment

# Register your models here.


admin.site.register(Post) # Admin sayfasında modelimizi görünür kılabilmek için, modeli admin.site.register(Post) ile kaydetmemiz gerekiyor.
admin.site.register(Comment)
