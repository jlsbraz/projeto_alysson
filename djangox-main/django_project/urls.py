from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="email/signup"), name="home"),
    path("login", TemplateView.as_view(template_name="account/login.html"), name="login"),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
