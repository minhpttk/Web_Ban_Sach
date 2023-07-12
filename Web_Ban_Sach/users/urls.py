from django.urls import path
from users import views as user_views
urlpatterns = [
    # path('Register/',include('Register.urls')),
    # path("profile/", user_views.profile, name="profile"),
    path("register/", user_views.register, name="login"),
    # path(
    #     "login/",
    #     auth_views.LoginView.as_view(template_name="users/login.html"),
    #     name="login",
    # ),
    # path(
    #     "logout/",
    #     auth_views.LogoutView.as_view(template_name="users/logout.html"),
    #     name="logout",
    # ),
]