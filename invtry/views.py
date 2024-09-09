from django.shortcuts import render
from django.http import JsonResponse
from . models import Drug
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import plotly.graph_objects as go
import plotly.io as pio

# Create your views here.


def inventory(request):
    return render(request , 'inventory.html')

@csrf_exempt
@require_POST
def add_drug(request):
    data = json.loads(request.body)
    drug = Drug.objects.create(
        drugid=data['drug_id'],
        name=data['name'],
        manufacturer=data['manufacturer'],
        drugtype=data['drug_type'],
        quantity=data['quantity'],
        expirydate=data['expiry_date'],
        description=data['description'],
        batchno=data['batch_no']
    )
    return JsonResponse({'status':'success', 'drugid':drug.drugid})

@csrf_exempt
@require_POST
def delete_drug(request):
    data = json.loads(request.body)
    drugid = data['drug_id']
    try:
        drug = Drug.objects.get(drugid=drugid)
        drug.delete()
        return JsonResponse({'status': 'success'})
    except Drug.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Drug not found'})

@csrf_exempt
@require_POST
def update_drug(request):
    data = json.loads(request.body)
    drugid = data['drug_id']
    try:
        drug = Drug.objects.get(drugid=drugid)
        drug.name = data['name']
        drug.manufacturer = data['manufacturer']
        drug.drugtype = data['drug_type']
        drug.quantity = data['quantity']
        drug.expiry_date = data['expiry_date']
        drug.description = data['description']
        drug.batchno = data['batch_no']
        drug.save()
        return JsonResponse({'status': 'success'})
    except Drug.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Drug not found'})

def drug_list(request):
    if request.method == 'GET':
        drugs = Drug.objects.all().values()
        return JsonResponse(list(drugs), safe=False)

def dashboard(request):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], y=[1, 4, 9, 36, 25], mode='lines+markers'))
    fig.update_layout(title='Medicine Trends', xaxis_title='Week', yaxis_title='Sales')
    graph_html = pio.to_html(fig, full_html=False)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], y=[1, 5, 10, 20, 25], mode='lines+markers'))
    fig.update_layout(title='Forecast', xaxis_title='Week', yaxis_title='Sales')
    forcast_html = pio.to_html(fig, full_html=False)

    return render(request, 'dashboard.html', {'graph_html': graph_html , 'forecast_html':forcast_html})
