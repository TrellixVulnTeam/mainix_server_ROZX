from django.conf.urls import url , include
from . import views

urlpatterns = [  # url(r'^$',views.mainpage),
    url(r'', views.crypto_main),

]