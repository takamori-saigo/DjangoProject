from django.shortcuts import render
from .models import * 

def getMainPage(request):
    return render(request, 'MainPython/mainPage.html', {'Main_Page_Content': MainPageContent.objects.first()})


def general_statistics(request):
    return render(request, 'MainPython/general_terms.html', {'statistic': Statistic.objects.prefetch_related('tables').all()})