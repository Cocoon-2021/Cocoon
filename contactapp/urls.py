from django.urls import path
from contactapp import views
urlpatterns=[
    path('',views.page),
    path('reg/',views.db1)
]