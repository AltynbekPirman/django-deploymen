from django.conf.urls import url
from landing import views
app_name="landing"

urlpatterns = [
    url(r'^$', views.form_page, name="formpage"),
]
