from re import template
from xml.dom.minidom import Document
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_view.LoginView.as_view(template_name='signin.html'), name='signin'),
    path('signout/', auth_view.LogoutView.as_view(template_name='signout.html'), name='signout'),
    path('viewandadd/', views.viewandadd, name='viewandadd'),
    path('edit_book/<str:pk>', views.edit_book, name='edit_book'),
    path('delete_book/<str:pk>', views.delete_book, name='delete_book'),
    path('deletereview/<str:book_id>/<str:review_id>',views.deletereview,name="deletereview"),
    path('cart/', views.cart, name='cart'),
    path('deleteitem/<str:cart_item_id>', views.deleteitem, name='deleteitem'),
    path('check_out/', views.check_out, name='check_out'),
    path('deleteorder/<str:order_id>', views.deleteorder, name='deleteorder'),
    path('danhanhang/<str:order_id>', views.danhanhang, name='danhanhang'),
    path('history_order/', views.history_order, name='history_order'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)