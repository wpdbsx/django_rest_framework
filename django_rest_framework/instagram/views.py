from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,action
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadonly
from rest_framework.filters import SearchFilter,OrderingFilter
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
    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated,IsAuthorOrReadonly]
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields= ['message']
    # ordering_fields=['id']
    # ordering=['id']
    def perform_create(self,serializer):
        # FIXME: 인증이 되어있다는 가정하에, author를 지정하겠습니다.
        author = self.request.user   # User or AnonymousUser
        ip= self.request.META['REMOTE_ADDR'] 
        serializer.save(ip=ip ,author=author )
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

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes= [TemplateHTMLRenderer]
    template_name= 'instagram/post_detail.html'

  
    def get(self,request,*args, **kwargs):
        post =self.get_object() 
        
        return Response({
            "post" :PostSerializer(post).data,
        })