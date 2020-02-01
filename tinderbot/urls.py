from django.urls import path
from django.conf.urls import url, include
from .views import HomePageView

urlpatterns = [
          
              path('', HomePageView.as_view(), name='home'),
              url(r'^submit', HomePageView.submit),
              

]