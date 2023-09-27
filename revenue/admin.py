from django.contrib import admin
from .models import RevenueStatistic
from spend.models import SpendStatistic

admin.site.register(RevenueStatistic)
admin.site.register(SpendStatistic)