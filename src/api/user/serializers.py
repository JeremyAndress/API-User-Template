from rest_framework import serializers

class UserSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   username = serializers.CharField()
   firstName = serializers.CharField(source='first_name')
   lastName = serializers.CharField(source='last_name')
   email = serializers.CharField()
   age = serializers.IntegerField()
