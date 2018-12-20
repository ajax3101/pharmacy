from django.http import JsonResponse

from .models import Pharmacy, Drug
from pharmacy.serializers import PharmacySerializer, DrugSerializer

def client_get_pharmacys(request):
    pharmacys = PharmacySerializer(
        Pharmacy.objects.all().order_by('-id'),
        many=True,
        context={'request':request}
    ).data

    return JsonResponse({'pharmacys': pharmacys})

def client_get_drugs(request, pharmacy_id):
    drugs = DrugSerializer (
        Drug.objects.all().filter(pharmacy_id=pharmacy_id).order_by('-id'),
        many=True,
        context={'request':request}
    ).data
    
    return JsonResponse({'drugs': drugs})
