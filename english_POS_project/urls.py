from django.urls import path
from . import views

urlpatterns = [

 path('', views.dashboard, name = "dashboard"),
 #path("signup/", views.SignUp.as_view(), name="signup"),
 #path("password_reset", views.password_reset_request, name="password_reset"),
 path("upload_file", views.upload_file, name="upload_file" ),
 path("submit_sentence", views.submit_sentence, name="sumbit_sentence")
]

