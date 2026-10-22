from django.shortcuts import render
from socialmedia_app.models import *
from socialmedia_app.serializers import *
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from socialmedia_app.permissions import IsOwner
from rest_framework.exceptions import ValidationError
# Create your views here.

class SignUpView(CreateAPIView):
    serializer_class=UserSerializer


class PostCreateListView(CreateAPIView,ListAPIView):
    serializer_class=PostSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    queryset=Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=PostSerializer
    queryset=Post.objects.all()

class UserRetrieveView(RetrieveAPIView):
    serializer_class=UserRetrieveSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=CustomUser.objects.all()

class CommonPostwallView(ListAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    serializer_class=PostSerializer
    queryset=Post.objects.all()


class CommentCreateListView(CreateAPIView,ListAPIView):
    serializer_class=CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentRetrieveDestoryView(RetrieveAPIView,DestroyAPIView):
    serializer_class=CommentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Comment.objects.all()

class LikeCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Like.objects.all()


    def perform_create(self, serializer):
        post_obj=serializer.validated_data['post_obj']
        if Like.objects.filter(post_obj=post_obj,owner_obj=self.request.user).exists():
            raise ValidationError("you liked already")
        serializer.save(owner_obj=self.request.user)

class UnLike(DestroyAPIView):
    serializer_class=LikeSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsOwner]
    queryset=Like.objects.all()

class FollowingView(CreateAPIView,ListAPIView):
    serializer_class=FollowSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Follow.objects.all()

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class UnFollowView(DestroyAPIView):
    serializer_class=FollowSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Follow.objects.all()

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)