from django.conf.urls import include, url
from app.records.views import songs

app_name = 'app_name'

urlpatterns=[

    url(r'^songs/$', songs, name='all-songs'),


    ]
