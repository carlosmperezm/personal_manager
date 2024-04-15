from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',include('todo.urls')),
    path('contact/',include('contact.urls')),
    path('',views.index,name='index')

]
