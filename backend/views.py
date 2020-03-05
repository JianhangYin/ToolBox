from django.http import HttpResponse
import json
import backend.meal_problem.get_recipe as gr
import backend.meal_problem.web_scraping as ws
import backend.meal_problem.mixed_integer_programming as mip


def get_five_recipe(request):
    dic = {'recipe': gr.getting()}
    return HttpResponse(json.dumps(dic))


def web_scraping(request):
    ws.scraping()
    return HttpResponse('Updated!')


def post_meal_planning(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        name_a = body.get('nameA', '')
        name_b = body.get('nameB', '')
        time_a = body.get('timeA', [])
        time_b = body.get('timeB', [])
        food_a = body.get('foodA', [])
        food_b = body.get('foodB', [])
        food_list = body.get('foodList', [])
        time_list_a = []
        time_list_b = []
        week_dict = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for day in week_dict:
            if day in time_a:
                time_list_a.append(1)
            else:
                time_list_a.append(0)
            if day in time_b:
                time_list_b.append(1)
            else:
                time_list_b.append(0)
        budget = body.get('budget', '0')
        dic = mip.programming(
            115,
            [time_list_a, time_list_b],
            int(budget),
            [name_a, name_b],
            food_list,
            food_a,
            food_b
        )
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse('post needed')
