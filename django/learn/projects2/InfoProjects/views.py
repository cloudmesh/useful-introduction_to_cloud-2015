#from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
#from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from InfoProjects.models import InfoProject
from InfoProjects.serializers import InfoProjectSerializer
#from django_tables2   import RequestConfig
#from InfoProjects.models  import InfoProject
#from InfoProjects.tables import NameTable

# Create your views here.

#def info_projects(request):
	
    #info = [
'''class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)'''

#@api_view(['GET', 'POST'])
#@renderer_classes((TemplateHTMLRenderer))
class InfoProject_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """

    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request, format=None):
        infoprojects = InfoProject.objects.all()
        serializer = InfoProjectSerializer(infoprojects, many=True)
        return Response({'project':serializer.data}, template_name='template_example.html' ) 

    def post(self, request, format='.html'):
        serializer = InfoProjectSerializer(data=request.DATA)
        if serializer.is_valid():
    	    serializer.save()
    	    return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
        
#@csrf_exempt
class InfoProject_detail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self,pk): 
        try:
            return InfoProject.objects.get(pk=pk)
        except InfoProject.DoesNotExist:
            raise Http404

    def get(self,request, pk, format=None):
	infoproject1 = self.get_object(jk)
        serializer = ProjectInfoSerializer(infoproject1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        infoproject1 = self.get_object(pk)
        serializer = InfoProjectSerializer(infoproject1, data=request.DATA)
        if serializer.is_valid():
    	    serializer.save()
    	    return Response(serializer.data)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        infoproject1 = self.get_object(pk)
	infoproject1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''class UserDetail(generics.RetrieveAPIView):

    queryset = InfoProject.objects.all()
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request):
	self.object= self.get_object()
	return Response ({'user':self.object}, template_name='template_example')'''
	
     		#]

#table = NameTable(info)
#RequestConfig(request).configure(table)
#return render(request, "template_example.html", {'table': table})'



