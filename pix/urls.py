from django.conf.urls import url
from . import views

urlpatterns=[
     url(r'^$', views.gallery, name='gallery'),
     url('^today/$',views.photos,name='gallery'),
     url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'gallery') 
]