from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import csv
import pandas as pd


array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

def file_open(request):
    csv_path = 'data/test_data.CSV'
    df = pd.read_csv(csv_path, encoding='cp949')
    data = df.to_dict('records')
    return JsonResponse({'dat':data})

def file_open2(request):
    csv_path = 'data/test_data_has_null.CSV'
    df = pd.read_csv(csv_path, encoding='cp949')
    df.fillna('NULL',inplace=True)
    data = df.to_dict('records')
    return JsonResponse({'dat':data})