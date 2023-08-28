from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, UserListView, ActivateUser
from servise.views import HomeView
from users.apps import UsersConfig
app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="regyster"),
    path("userslist/", UserListView.as_view(), name="userslist"),
    path("userbloc/<int:pk>/", ActivateUser, name="block")
]