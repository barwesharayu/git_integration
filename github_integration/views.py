from django.shortcuts import render, HttpResponse
import requests
import json
from .models import repo_issues
from datetime import datetime, timedelta

from django.utils.datastructures import MultiValueDictKeyError


def index(request):
    repo = requests.get('https://api.github.com/repos/pallets/jinja/issues')
    t = repo.json()

    repo_issues.objects.all().delete()
    for i in t:
        s1 = i['state']
        d1 = i['created_at'][:10]
        try:
            a1 = i['user']['id']
        except:
            a1 = None
        try:
            l1 = i['labels'][0]['id']
        except:
            l1 = None
        d1 = {'user': a1, 'state': s1, 'labels': l1, 'create_date': d1}
        # list1.append(d1)
        # Repo1 = repo_issues(assignee= a1, state = s1, labels = l1)
        Repo1 = repo_issues(**d1)
        Repo1.save()

    filter1 = request.GET.get('filters')
    print(filter1)
    val = request.GET.get('e_Value')
    print(val)
    if filter1 == 'State':
        R1 = repo_issues.objects.filter(state=val)
    elif filter1 == 'User':
        R1 = repo_issues.objects.filter(user=val)
    elif filter1 == 'label':
        R1 = repo_issues.objects.filter(labels=val)
    elif filter1 == 'Days':
        d = datetime.today() - timedelta(days=int(val))
        R1 = repo_issues.objects.filter(create_date__gt=d)
        print(d)
    elif filter1 == 'All':
        R1 = repo_issues.objects.all()

    return render(request, 'index.html', {'R1': R1})
