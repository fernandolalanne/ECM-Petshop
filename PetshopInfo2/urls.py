from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    # path('',views.accueil, name="accueil"),
    path('accueil',views.accueil, name="accueil"),
    path('', views.signin, name='signin'),
    path('inicio',views.inicio, name="inicio"),
    path('accounts',views.accounts, name="accounts"),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('terminer_la_session', views.terminer_la_session, name='terminer_la_session'),

    
    # shops
    path('shops',views.shops,name='shops'),
    path('index2',views.index2,name='index2'),

    


    #admin
    path('admin',views.admin,name='admin'),

    # status animals
    path('update_pet/<str:pet_name>/', views.update_pet, name='update_pet'),

    # cart
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),

    path('buy/', views.buy_items, name='buy_items'),

    path('get_cart_count/', views.get_cart_count, name='get_cart_count'),

    path('delete_item/<str:item_name>/', views.delete_item, name='delete_item'),

]