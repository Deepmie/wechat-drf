"""backproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import app01.views as views
from rest_framework import routers
import rest_framework.authtoken.views as authtokenviews
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register('baseuser',views.UserView,basename='baseuser')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getoken/',authtokenviews.obtain_auth_token),
    path('test/',include('app01.urls',namespace='son')),
]
urlpatterns+=router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)