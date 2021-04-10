from django.contrib import admin
from django.urls import path

from crud_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('', Read.as_view(), name='read'),
]
