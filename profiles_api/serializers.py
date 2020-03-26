from rest_framework import serializers

from profiles_api import models

class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing serializer for our api  """
    name=serializers.CharField(max_length=10)
#-------------------------------------------------------------------------------
class UserProfileSerializer(serializers.ModelSerializer):
    """ serializes a name field or  testing our APIView """
    class Meta:
        """docstring forMeta."""
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
        'password':{
        'write_only':True, 'style':{'input_type': 'password'} }
        }

    def create(self, validated_data):
        """Used to create a new user"""
        user = models.UserProfile.objects.create_user(
                email=validated_data['email'],
                name=validated_data['name'],
                password=validated_data['password']
                )
        return user

#user.set_password(validated_data['password'])
#user.save()