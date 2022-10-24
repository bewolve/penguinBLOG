from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from authuser import views as v

urlpatterns = [
    path("login/", v.loginuser, name="login"),
    path("logout/", v.logoutuser, name="logout"),
    path("", include("home.urls")),
    path("supers3cret4dm1n/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
