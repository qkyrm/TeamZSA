from django.urls import path, include
from users.views import Register
from users.views import Form
urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('form/', Form.as_view(), name="form"),
]
