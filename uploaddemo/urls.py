"""uploaddemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static,settings

urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('register/',views.CustomerRegistration.as_view(),name='register'),
    path('login/',views.CustomerLogin.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('cart/',views.MyCart.as_view(),name='cart'),
    path('detail/<int:id>',views.ProductDetail.as_view(),name='detail'),
    path('allcusts/',views.AllCustomers.as_view(),name='allcusts'),
    path('cats/',views.CategoryView.as_view(),name='cats'),
    path('products/',views.ProductView.as_view(),name='products'),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

