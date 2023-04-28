from .models import *
from rest_framework import serializers





# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Author
#        fields = ['id','name']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Category
       fields = ['id', 'name']

class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'categoryType', 'dateCreation', 'title', 'postCategory', 'text', ]




