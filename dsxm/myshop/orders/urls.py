from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  url(r"^confirm/$", views.confirm, name="confirm"),
                  url(r"^pay/$", views.pay, name="pay"),
                  url(r"^done/$", views.done, name="done"),
                  url(r"^list/$", views.list, name="list"),
                  url(r"^drop/$", views.drop, name="drop"),
                  url(r"^(?P<o_id>\d+)/detail/$", views.detail, name="detail"),
              ]