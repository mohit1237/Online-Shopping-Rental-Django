from django.conf.urls import include, url
from . import views

app_name = 'welcome'

urlpatterns = [
	#/game
    url(r'^$',views.index, name='index'),
    url(r'^cart/$',views.cart, name='cart'),
    url(r'^checkout/step1/$',views.checkoutStep1, name='step1'),
    url(r'^checkout/step2/$',views.checkoutStep2, name='step2'),
    url(r'^checkout/step3/$',views.checkoutStep3, name='step3'),

    ]