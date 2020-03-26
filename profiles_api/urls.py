from django.urls import path
from profiles_api import views

from django.urls import include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
#http://127.0.0.1:8000/api/hello-viewset/
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# base_name only if in views queryset = models.UserProfile.objects.all()
# does not exists
#http://127.0.0.1:8000/api/profile/
router.register('profile', views.UserProfileViewSet )

urlpatterns=[
#http://127.0.0.1:8000/api/hello-view/
path('hello-view/',views.HelloApiView.as_view()),
#http://127.0.0.1:8000/api/login/
path('login/',views.UserLoginApiView.as_view()),

path('',include(router.urls) ),
]
