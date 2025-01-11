from django.shortcuts import render
from .models import Property


def property_list(request):
    query = request.GET.get('query', '')
    if query:
        properties = Property.objects.filter(location__icontains=query)
    else:
        properties = Property.objects.filter(is_published=True)
    return render(request, 'property_list.html', {'properties': properties})


def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'property_detail.html', {'property': property})

def index(request):
    return render(request, 'index.html')
# Create your views here.
