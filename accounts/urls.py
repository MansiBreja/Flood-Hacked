from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    url(r"^login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$", views.SignUp.as_view(), name="signup"),
    url(r'^diagnosis_detail/new/$',views.addloc,name='addloc'),
    url(r'^findcoordinates/$',views.findcoordinates,name='findcoordinates'),
    url(r'^inputhelicopdrones/$',views.inputhelicopdrones,name='inputhelicopdrones'),
]
