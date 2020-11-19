from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,action
# Create your views here.

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all().filter(is_public=True) # filter(is_public=True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self,requeest):
#         qs = Post.objects.filter(is_public=True) 
#         serializer = PostSerializer(qs,many=True)
#         return Response(serializer.data)
# public_post_list = PublicPostListAPIView.as_view()

@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True) 
    serializer = PostSerializer(qs,many=True)
    return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class= PostSerializer

    def dispatch(self,request,*args,**kwargs) :
        print("request.body:",request.body) # print 비추천, logger 추천
        print("request.POST",request.POST)
        return super().dispatch(request,*args,**kwargs)

    @action(detail=False,methods=['GET']) 
    def public(self,request):
        qs = self.get_queryset().filter(is_public=True) 
        serializer = self.get_serializer(qs,many=True)
        return Response(serializer.data) 
    
    @action(detail=True,methods=['PATCH'])
    def set_public(self,request,pk):
        instance= self.get_object()
        instance.is_public = True 
        instance.save(update_fields=['is_public']) 
        serializer = self.get_serializer(instance) 
        return Response(serializer.data)

# def post_list(request):
#     pass

# post_list= csrf_exempt(post_list) #고차 컴포넌트(Higher Order Component)