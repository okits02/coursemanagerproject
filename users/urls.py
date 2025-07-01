from django.urls import path
from .views import RegisterView, LoginView, UserView, UpdateProfileView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("user/", UserView.as_view(), name="user"),
    path('update-profile/', UpdateProfileView.as_view(), name='update_profile'),
]