from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_index, name='contact_index'),
    path('<str:letter>', views.contact_index, name='contact_index'),
    path('view/<int:id>', views.contact_view, name='contact_view'),
    path('edit/<int:id>', views.update_contact, name='update_contact'),
    path('create', views.create_contact, name='create_contact'),
    path('delete/<int:id>',views.delete_contact,name='delete_contact')
]
