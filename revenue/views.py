from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RevenueStatistic


class RevenueAPI(APIView):

    def get(self, request):
        statistic = RevenueStatistic.objects.values('name', 'date',
                                                    'revenue', 'spend__spend',
                                                    'spend__impressions', 'spend__clicks',
                                                    'spend__conversion')
        total_revenue = RevenueStatistic.objects.aggregate(total_revenue=Sum('revenue'))
        response_data = {
            'total_revenue': total_revenue['total_revenue'],
            'data': list(statistic),
        }
        return Response(response_data)
