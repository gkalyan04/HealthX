from django.conf.urls import url
from home import views

app_name = 'home'

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^nearby/',views.nearby,name='nearby'),

]
