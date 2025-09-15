from django.shortcuts import render
from tasks.models import Tasks
from rest_framework import generics
from .serializers import TaskSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

# Create your views here.

class isAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        #obj model instance that calls the permission, .owner is the attribute
        return obj.owner == request.user #nb request user is current authenticated user object that DRF provides 


def index(request):
    try:
        tasks = Tasks.objects.all() #ORM 
        #parameter
        # Tasks.objects.filter(description="reruffrufber").get()
        #SELECT * FROM Tasks
        #SELECT * FROM Tasks where desrcription= "---" 
        return render(request, 'tasks/index.html',{'tasks' : tasks})
    except Exception as e:
        raise e
    
def detail_view(request, pk):
    try:
        task = Tasks.objects.get(pk = pk)
        return render(pk, 'tasks/task.html', { 'task' : task})
    except Exception as e:
        raise e
    
    
class TaskListCreate(generics.ListCreateAPIView): #get all tasks, and post a single task 
    queryset  = Tasks.objects.all()
    serializer_class = TaskSerializer
    print("<<<>>>",serializer_class)
    
    
    
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):  #get, put, patch, delete  for one task
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [ IsAuthenticated,IsAdminUser ]
    
    
    

# @api_view(method=["GET"])
# def show_all_tasks(request):
#     all_tasks = TaskListCreate(Tasks.objects.all(), many=True)
    
#     return Response({"message": "Data fetched successfully", "data": all_tasks.data}, status=200)
    

# @api_view(method=["PUT"])
# def get_task(request, pk):
#     description = request.data.get("description")
#     if pk:
#         task = Tasks.objects.get(pk=pk)
#         task.
#         return Response({"message": "Data updated successfully", "data": task.data}, status=200)
    
    
    