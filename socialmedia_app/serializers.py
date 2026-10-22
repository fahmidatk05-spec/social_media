from rest_framework import serializers
from socialmedia_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=["id","username","email","password","phone"]
        read_only_fields=["id"]
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"
        read_only_fields=["id","added_at","owner"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Like
        fields="__all__"
        read_only_fields=["id","created_at","owner_obj","post_obj"]
    
class PostSerializer(serializers.ModelSerializer):
    comment_count=serializers.SerializerMethodField()
    like_count=serializers.SerializerMethodField()
    comment=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields="__all__"
        read_only_fields=["id","created_at","owner"]

    def get_comment_count(self,obj):
        return Comment.objects.filter(post_obj=obj).count()

    def get_like_count(self,obj):
        return Like.objects.filter(post_obj=obj).count()

    def get_comment(self,obj):
        comments=Comment.objects.filter(post_obj=obj)
        return CommentSerializer(comments,many=True).data 


class UserRetrieveSerializer(serializers.ModelSerializer):
    post=PostSerializer(many=True,read_only=True)
    post_count=serializers.SerializerMethodField()
    class Meta:
        model=CustomUser
        fields=["id","username","post","post_count"]
        read_only_fields=["id","username","post"]

    def get_post_count(self,obj):
        return Post.objects.filter(owner=obj).count

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields="__all__"
        read_only_fields=["id","follower"]