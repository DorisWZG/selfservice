from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from budget_allocation.models import Channel,Industry, PriceMetrics
from budget_allocation.serializers import ChannelSerializer, IndustrySerializer, PriceMetricsSerializer

# Create your views here.
def budget_allocation_test(request):
    return render(request, 'budget_allocation/stage2_test.html', {})
def stage2_result(request):
    return render(request, 'budget_allocation/stage2_result.html', {})



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