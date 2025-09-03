from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(
        pattern_name="ni_list", permanent=False), name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    # Nutritional Information
    path("nutritional-info/", views.ni_list, name="ni_list"),
    path("nutritional-info/create/", views.ni_create, name="ni_create"),
    path("nutritional-info/<int:pk>/", views.ni_detail, name="ni_detail"),
    path("nutritional-info/<int:pk>/edit/", views.ni_update, name="ni_update"),
    path("nutritional-info/<int:pk>/delete/",
         views.ni_delete, name="ni_delete"),
]
