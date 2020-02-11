from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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

def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        #Formun doğruluğunu kontrol ediyoruz ve doğru ise kaydedebiliriz!
        if form.is_valid():
            post = form.save(commit = False) #Post modelini henüzkaydetmek istemiyoruz demektir
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk = post.pk) #post_detail, gitmek istediğimiz view'ın adı.
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete() #  Every Django model can be deleted by .delete() 
    #
    return redirect('post_list')
