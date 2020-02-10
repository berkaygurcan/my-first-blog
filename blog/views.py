from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
#Burada post_list isimli 
# bir fonksiyon (def) yarattık, 
# bu fonksiyon girdi olarak request (isteği) alıp, blog/post_list.html template'ini işleyecek olan render fonksiyonunu döndürüyor.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
