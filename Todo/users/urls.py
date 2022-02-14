from django.urls import path, include
#from .views import UserRegisterView
from .import views
 
urlpatterns = [
    #path('register/', UserRegisterView.as_view(), name="register")
    #path('login_user', views.login_user, name="login"),
    path('', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register"),
    path('todo_list', include('todoApp.urls')),

    #path('login/', views.login_view, name="login"),

]

    #path('sign_user', views.login_user, name="login"),
    #path('logout_user', views.logout_user, name="logout"),
    #path('register_user', views.register_user, name="register"),
