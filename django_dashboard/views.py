from django.shortcuts import render
from .models import Drug  # Import your Drug model
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Consumption
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! Welcome to my Django project.")

def expiring_soon_drugs(request):
    today = datetime.today().date()  # Get today's date
    soon = today + timedelta(days=30)  # 30-day threshold
    urgent = today + timedelta(days=7)  # 7-day threshold for urgent expiration

    # Query for drugs that will expire within the next 30 days
    expiring_drugs = Drug.objects.filter(expiry_date__range=[today, soon])
    urgent_drugs = Drug.objects.filter(expiry_date__range=[today, urgent])  # Urgently expiring

    return render(request, 'expiring_drugs.html', {
        'expiring_drugs': expiring_drugs,
        'urgent_drugs': urgent_drugs
    })

@api_view(['GET'])
def consumption_trend(request, drug_id):
    # Get the consumption data for the drug
    consumption_data = Consumption.objects.filter(drug__drug_id=drug_id).order_by('date')

    # Format the data to be JSON serializable
    data = {
        'dates': [cons.date.strftime('%Y-%m-%d') for cons in consumption_data],
        'quantities': [cons.quantity for cons in consumption_data]
    }
    return JsonResponse(data)
@api_view(['GET'])
def top_five_most_purchased(request):
    # Get the total quantity purchased per drug and order by quantity in descending order
    top_five = (
        Consumption.objects.values('drug__name')  # Get the drug name
        .annotate(total_quantity=Sum('quantity'))  # Sum up the quantities per drug
        .order_by('-total_quantity')[:5]  # Limit to the top 5
    )

    # Prepare the data to be sent as JSON
    data = {
        'drugs': [item['drug__name'] for item in top_five],
        'quantities': [item['total_quantity'] for item in top_five]
    }

    return JsonResponse(data)