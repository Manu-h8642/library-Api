from django.conf.urls import url
from libapp import views

urlpatterns = [
    url(r'^lib/$',views.libapi)
]