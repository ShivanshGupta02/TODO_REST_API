# from django.shortcuts import render
# Create your views here.

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import  TokenAuthentication
from django.shortcuts import get_object_or_404



#  api_view is a decorator that modifies the exisiting functionality of a function

@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status':200,
            'message':'Yes! Django rest framework is working',
            'metod_called ': 'You called GET method',
        })
    elif request.method == 'POST':
        return Response({
            'status':200,
            'message':'Yes! Django rest framework is working',
            'metod_called ': 'You called POST method',
        })
    elif request.method=='PATCH':
        return Response({
            'status':200,
            'message':'Yes! Django rest framework is working',
            'metod_called ': 'You called PATCH method',
        })
    else:
        return Response({
            'status':400,
            'message':'Yes! Django rest framework is working',
            'metod_called ': 'You called invalid method',
        })
        
        
from .serializer import *
from .models import Todo

# ------------ FUNCTION BASED VIEW -----------------

@api_view(['GET'])
def get_todo(request):
    data = Todo.objects.all()
    serializer = TodoSerializer(data,many=True)
    return Response(({
        'status':True,
        'message': 'Todo data fetched',
        'data': serializer.data
    }))

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            # print(serializer.data)
            serializer.save()
            return Response({
                'status':True,
                'message':'Success data',
                'data': serializer.data 
            })
    except Exception as e:
        print(e)
    return Response({
            'status': False,
            'message':'invalid data',
            'data' : serializer.errors,
        })
    

@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data 
        if not data.get('uid'):
            return Response({
                'status': False,
                'message' : 'uid is required',
                'data' : {}
            })
    
        obj = Todo.objects.get(uid=data.get('uid'))
        serializer = TodoSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : True,
                'message' : 'Success',
                'data' : serializer.data
            })
        
        return Response({
            'status':False,
            'message' : 'Data is not valid',
            'data' : serializer.errors
        })
    
    except Exception as e:
        print(e)
    return Response({
        'Status' : False,
        'message' : 'Invalid uid',
        'data' : {}
    })
    
from rest_framework.views import APIView  
from django.contrib.auth.models import User

# ---------- CLASS BASED VIEW -----------

# Main drawback of APIview inherited subclass based view is that it supports
# only 5 methods : GET, POST, PUT, PATCH, DELETE

class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        print(request.user)
        data = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(data,many=True)
        return Response(({
            'status':True,
            'message': 'Todo data fetched',
            'data': serializer.data
        }))
        
    def post(self,request):
        try:
            data = request.data
            data["user"] = request.user.id
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                # print(serializer.data)
                serializer.save()
                return Response({
                    'status':True,
                    'message':'Success data',
                    'data': serializer.data 
                })
        except Exception as e:
            print(e)
        return Response({
                'status': False,
                'message':'invalid data',
                'data' : serializer.errors,
            })
    
    def patch(self,request):
        try:
            data = request.data 
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message' : 'uid is required',
                    'data' : {}
                })
        
            obj = Todo.objects.get(uid=data.get('uid'))
            serializer = TodoSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : True,
                    'message' : 'Success',
                    'data' : serializer.data
                })
            
            return Response({
                'status':False,
                'message' : 'Data is not valid',
                'data' : serializer.errors
            })
        
        except Exception as e:
            print(e)
        return Response({
            'Status' : False,
            'message' : 'Invalid uid',
            'data' : {}
        })
        
    def delete(self,request):
        try:
            data = request.data 
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message' : 'uid is required',
                    'data' : {}
                })
        
            # Todo.objects.filter(uid=data.get('uid')).delete()
            instance=get_object_or_404(Todo,uid=data.get('uid'))
            instance.delete()
            return Response({
                'status' : True,
                'message' : 'Successfully deleted',
            })
        
        except Exception as e:
            print(e)
        return Response({
            'Status' : False,
            'message' : 'Invalid uid, Please enter valid uid',
            'data' : {}
        })
        


# -----------------------------------------------------
# --------------- VIEWSETS ----------------------------
# Viewset supports additional custom method apart from 5 methods(put,post,patch,get,delete)
# Using 'actions' , custom method can be written
from rest_framework import status, viewsets 
from rest_framework.decorators import action

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False,methods=['GET'])
    def get_timing_todo(self,request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs,many=True)
        return Response({
            'status' : True,
            'message' : 'Success',
            'data' : serializer.data
        })
    
    @action(detail=False, methods=['post'])
    def add_date_to_todo(self,request):
        try:
            data = request.data 
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Success',
                    'data' : serializer.data
                })
            return Response({
                'status' : False,
                'message' : 'Data is not valid',
                'data' : serializer.errors  
            })
        except Exception as e:
            print(e)
            
        return Response({
            'status' : False,
            'message' : 'Something went wrong!!'
        })