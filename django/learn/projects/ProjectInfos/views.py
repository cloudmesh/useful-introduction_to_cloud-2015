#from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ProjectInfos.models import ProjectInfo
from ProjectInfos.serializers import ProjectInfoSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
@csrf_exempt
def ProjectInfo_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        projectinfos = ProjectInfo.objects.all()
        serializer = ProjectInfoSerializer(projectinfos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
        
        
@csrf_exempt
def ProjectInfo_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        projectInfo = ProjectInfo.objects.get(pk=pk)
    except ProjectInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectInfoSerializer(projectInfo)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProjectInfoSerializer(projectInfo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        projectInfo.delete()
        return HttpResponse(status=204)
