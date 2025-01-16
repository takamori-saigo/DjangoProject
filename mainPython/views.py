from django.shortcuts import render
from .models import * 
from .get_last_vacancies import get_last_vacancies

def geography_statistics(request):
    return render(request, 'MainPython/geography_statistic.html', {'statistic': Geography_statistic.objects.prefetch_related('tables').all()})

def getMainPage(request):
    return render(request, 'MainPython/mainPage.html', {'Main_Page_Content': MainPageContent.objects.first()})

def demand(request):
    return render(request, 'MainPython/demand.html', {'statistic': Demand_statistic.objects.prefetch_related('tables').all()})

def general_statistics(request):
    return render(request, 'MainPython/general_terms.html', {'statistic': Statistic.objects.prefetch_related('tables').all()})

def skills_statistics(request):
    return render(request, 'MainPython/skills_statistic.html', {'statistic': Skills_statistic.objects.prefetch_related('tables').all()})

def recent_jobs(request):
    try: vacancies = get_last_vacancies()
    except Exception as e:
        vacancies = []
        print(f"Ошибка: {e}")
        
    return render(request, 'MainPython/recent_works.html', {'vacancies': vacancies})