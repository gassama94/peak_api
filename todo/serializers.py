from rest_framework import serializers
from .models import Todo, Profile



class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    # field = ('id', 'title', 'description', 'completed')
    fields = '__all__' 


  def get_owner_profile(self, obj):
        return ProfileSerializer(obj.owner.profile, context=self.context).data
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'image', 'user']

class ProfileWithTodosSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'image', 'user', 'todos']

class TodoWithOwnerProfileSerializer(serializers.ModelSerializer):
    owner_profile = ProfileSerializer(source='owner.profile', read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
