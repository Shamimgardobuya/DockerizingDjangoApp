from tasks import views
from django.urls import path

urlpatterns = [
    path('', view=views.TaskListCreate.as_view(), name='all_tasks'),
    path('<int:pk>', view=views.TaskDetail.as_view(), name='task_detail')
]


