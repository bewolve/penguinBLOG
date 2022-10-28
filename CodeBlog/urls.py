from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from authuser import views as v

urlpatterns = [
    path("signup/", v.registerUser, name="signup"),
    path("login/", v.loginuser, name="login"),
    path("logout/", v.logoutuser, name="logout"),
    path("", include("home.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
