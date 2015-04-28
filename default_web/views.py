from django.http import HttpResponse
from django.shortcuts import render
from member_service.models import Product_Dictionary_C1, Product_Dictionary_C2, Product_Dictionary_C3
from member_service.views import get_market_trend
import json
# def getCat1(request):
#     all_cats = Product_Dictionary_C1.objects.all()
#     print all_cats
#     return render(request, all_cats)

def getCat(request):
    if request.method == 'GET':
        all_cats = Product_Dictionary_C1.objects.all()
        context = {'all_cat1': all_cats}
        # print context
    return render(request, 'default_web/stage1_test.html', context)


def getCat2(request, cat):
    all_cats2 = Product_Dictionary_C2.objects.filter(cat1_id__eng_kw = cat)
    result = []
    for cat2 in all_cats2:
        result.append({ 'eng_kw': cat2.eng_kw })
    return HttpResponse(json.dumps(result), content_type='application/json')
    # return render(request, 'default_web/stage1_test.html', context)
#
# def getCat3(cat2):
#     all_cats3 = Product_Dictionary_C3.objects.filter(cat2 = cat2)
#     return all_cats3
# print getCat1(), getCat2(cat1=getCat1()), getCat3(cat2=getCat2(cat1=getCat1()))


# def stage2_result(request, cat1, cat2, cat3):
#     result = get_market_trend(cat1, cat2, cat3)
#     context = {'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'trend_result': result}
#     return render(request, 'member_service/ssp.html', context)
#



def index(request):
    #return HttpResponse("Hello, world!")
    #return render_to_string('default_web/index.html',{})
    return render(request, 'default_web/index.html', {})

def product_and_service(request):
    return render(request, 'default_web/pns.html',{})

def about(request):
    return render(request, 'about.html',{})

def member_service(request):
    return render(request, 'member_service.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def education_case(request):
    return render(request, 'default_web/education_case.html',{})
def destination_mkt_case(request):
    return render(request, 'default_web/destination_mkt_case.html',{})
def real_estate_case(request):
    return render(request, 'default_web/real_estate_case.html',{})
def high_tech_case(request):
    return render(request, 'default_web/high_tech_case.html',{})


def market_test(request):
    return render(request, 'default_web/stage1_test.html', {})
def stage1_result(request):
    return render(request, 'default_web/stage1_result.html', {})

def budget_allocation_test(request):
    return render(request, 'default_web/stage2_test.html', {})
def stage2_result(request):
    return render(request, 'default_web/stage2_result.html', {})

def wave_test(request):
    return render(request, 'default_web/stage3_test.html', {})
def stage3_result(request):
    return render(request, 'default_web/stage3_result.html', {})






