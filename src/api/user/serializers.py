from rest_framework import serializers

class UserSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   username = serializers.CharField()
   firstName = serializers.CharField(source='first_name')
   lastName = serializers.CharField(source='last_name')
   email = serializers.CharField()
   age = serializers.IntegerField()

   def update(self, instance, validated_data):
      instance.username = validated_data.get('username', instance.username)
      instance.first_name = validated_data.get('first_name', instance.first_name)
      instance.last_name = validated_data.get('last_name', instance.last_name)
      instance.email = validated_data.get('email', instance.email)
      instance.age = validated_data.get('age', instance.age)
      instance.save()
      return instance
