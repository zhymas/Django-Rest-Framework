from django.contrib import admin
from django.urls import path
from revenue.views import RevenueAPI
from spend.views import SpendAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/revenue/', RevenueAPI.as_view()),
    path('api/spend/', SpendAPI.as_view())

]
