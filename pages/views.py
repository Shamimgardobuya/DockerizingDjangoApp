from django.shortcuts import render

# Create your views here. #logic happening
def index(request):
    return render(request, 'pages/todos.html', {})

