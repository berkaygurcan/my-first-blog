from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #Gördüğünüz üzere, ana URL'e post_list adında bir view atıyoruz
]
#Son kısım name='post_list', görünümü (view) tanımlamak için kullanılan URL'in adıdır. Bu view'un adı ile aynı olabilir ama tamamen farklı bir şey de olabilir.