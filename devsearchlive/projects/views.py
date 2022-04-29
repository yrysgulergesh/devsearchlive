from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
        'topRated': True
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work',
        'topRated': False
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community',
        'topRated': True
    }
]



def projects(request):
    # name = 'Yrysgul Ergesh'
    # age = 2    
        context = {'projects': projectsList}
        return render(request, 'projects/projects.html', context)
    
    
def project(request, pk):
    projectObject = None
    
    for i in projectsList:
        if i['id'] == str(pk):
            projectObject = 1
    return render(request, 'projects/single-projects.html', {'project': projectObject})
    
