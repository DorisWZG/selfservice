from django.shortcuts import render
from django.db import connection

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from budget_allocation.models import Channel,Industry, PriceMetrics
from budget_allocation.serializers import ChannelSerializer, IndustrySerializer, PriceMetricsSerializer

# Create your views here.
def budget_allocation_test(request):
    return render(request, 'budget_allocation/stage2_test.html', {})

def stage2_result(request, industry, sub_industry, budget):
    result = get_metrics(industry, sub_industry, budget)
    context = {'category_name': industry, 'budget': budget, 'metrics_result': result}
    return render(request, 'budget_allocation/stage2_result.html', context)

# search recommended media channels for selected industry
def recomm_channels(request, industry, sub_industry):
    recomm_channels = PriceMetrics.objects.filter(industryId__subIndustry=sub_industry)
    context = {'category_name': industry, 'subcategory_name':sub_industry,
               'metrics_result': recomm_channels, 'metrics_range': range(0, len(recomm_channels))}
    return render(request, 'budget_allocation/stage2_result.html', context)


@api_view(['GET', 'POST'])
def channel_list(request):

    if request.method == 'GET':
        channels = Channel.objects.all()
        serializer = ChannelSerializer(channels, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChannelSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def industry_list(request):
    if request.method == 'GET':
        industries = Industry.objects.all()
        serializer = IndustrySerializer(industries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IndustrySerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def metrics_list(request, industry, budget):
# def metrics_list(request):
    if request.method == 'GET':
        matrix = PriceMetrics.objects.all()
        serializer = PriceMetricsSerializer(matrix, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PriceMetricsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def industry_detail(request, pk):
    try:
        industry = Industry.objects.get(pk=pk)
    except Industry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IndustrySerializer(industry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IndustrySerializer(industry, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        industry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def industry_object(pk):
    industry = Industry.objects.get(pk=pk).lower()
    return industry

def budget(self):
    budget = PriceMetrics.objects.get(budget = self.budget)
    return budget

@api_view(['GET'])
def metrics_result(request, industry, sub_industry, budget):

    metrics_result = get_metrics(industry, sub_industry, budget)

    Result = []

    for items in metrics_result:
        items_detail = {}
        items_detail['channelName'] = items.channelId.channelName
        items_detail['allocation'] = items.allocation
        items_detail['expectedClicks'] = items.expectedClicks
        items_detail['costPerClick'] = items.costPerClick
        items_detail['expectedImpressions'] = items.expectedImpressions
        items_detail['costPerImpression'] = items.costPerImpression
        # items_detail['minMediaBuy'] = items.minMediaBuy
        Result.append(items_detail)

    # serializer = MetricsResultSerializer(Result,many=True)
    return Response(data=Result)


def get_metrics(industry, sub_industry, budget):
    # industry_result = list(Industry.objects.filter(subIndustry=sub_industry))[0]
    # metrics_result = industry_result.pricemetrics_set.filter(budget=budget)
    metrics_result = PriceMetrics.objects.filter(industryId__subIndustry=sub_industry).filter(budget=budget)
    return metrics_result


@api_view(['GET'])
def get_industryNameList(request):
    industryName_list = Industry.objects.values('industryName').distinct()
    return Response(data=industryName_list)


@api_view(['GET'])
def get_subIndustryList(request,industry):
    subIndustry_list =Industry.objects.values('subIndustry').filter(industryName=industry)
    return Response(data=subIndustry_list)

