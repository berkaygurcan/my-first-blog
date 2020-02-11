from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #Gördüğünüz üzere, ana URL'e post_list adında  bir view atıyoruz
    path('post/<int:pk>/',views.post_detail, name = 'post_detail'), #post/<int:pk>/ kısmı bir URL kalıbı belirtir
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    
]
#Son kısım name='post_list', görünümü (view) tanımlamak için kullanılan URL'in adıdır.
#  Bu view'un adı ile aynı olabilir ama tamamen farklı bir şey de olabilir.
# <int:pk> - bu bölüm daha zorlayıcı. Django'nun bir tamsayı değeri beklediği ve onu pk adlı bir değişken olarak bir görünüme(view) aktaracağı anlamına gelir.