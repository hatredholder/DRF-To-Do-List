from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	try:
		task = Task.objects.get(id=pk)
	except:
		return Response({"error":"Object does not exist"})
	serializer = TaskSerializer(task, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	try:
		task = Task.objects.get(id=pk)
	except:
		return Response({"error":"Object does not exist"})
	
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	try:
		task = Task.objects.get(id=pk)
	except:
		return Response({"error":"Object does not exist"})
	task.delete()

	return Response('Item succsesfully delete!')



