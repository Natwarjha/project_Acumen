from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameAgeSalaryForm
import requests
from django.http import JsonResponse
from django.conf import settings

def process_form(request):
    if request.method == 'POST':
        form = NameAgeSalaryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']
            response_text = f"{name} is {age} years old and earns {salary} every month."
            return HttpResponse(response_text)
        else:
            return render(request, 'myapp/form.html', {'form': form})
    else:
        form = NameAgeSalaryForm()
        return render(request, 'myapp/form.html', {'form': form})
    


def fetch_jokes(request):
    if request.method == 'POST':
        count = request.POST.get('count', '1')
        try:
            count = int(count)
            if count < 1:
                raise ValueError("Count must be a positive integer")
        except ValueError as e:
            return JsonResponse({'error': str(e)})

        url = f"https://api.api-ninjas.com/v1/jokes?limit={count}"
        headers = {'X-Api-Key': settings.API_NINJAS_KEY}
        response = requests.get(url, headers=headers)
        jokes = response.json()

        return render(request, 'myapp/jokes.html', {'jokes': jokes})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})

