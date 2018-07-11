from rest_framework import routers
from app_web import views
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register("user", views.UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^register/', views.RegisterView.as_view()),
    url(r'^identity_check/', views.login),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='博客系统API', permission_classes=(), authentication_classes=())),
]