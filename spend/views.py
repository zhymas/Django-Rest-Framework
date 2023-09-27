from rest_framework.views import APIView
from .models import SpendStatistic
from django.db.models import Sum
from rest_framework.response import Response



class SpendAPI(APIView):

    def get(self, request):
        statistic_spend = SpendStatistic.objects.select_related('revenue_statistic').values(
            'date', 'name', 'spend', 'impressions', 'clicks', 'conversion')

        total_spend = SpendStatistic.objects.aggregate(
            spend=Sum('spend'),
            impressions=Sum('impressions'),
            clicks=Sum('clicks'),
            conversion=Sum('conversion')
        )

        response_data = {
            'total_spend': {
                'spend': total_spend['spend'],
                'impressions': total_spend['impressions'],
                'clicks': total_spend['clicks'],
                'conversion': total_spend['conversion'],
            },
            'data': list(statistic_spend)
        }

        return Response(response_data)


