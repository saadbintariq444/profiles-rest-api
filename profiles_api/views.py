from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers
from rest_framework import status

from rest_framework import viewsets

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

#from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
#http://127.0.0.1:8000/api/hello-view/
class HelloApiView(APIView):
    """Test Api Views"""
    #serializer using
    serializer_class=serializers.HelloSerializers


    def get(self,request, format=None):
        """Returns a List of Api views """
        an_apiview=[
        'Uses HTTPS method as functions (get,post,patch,put,delete)',
        'Is similar to a Traditional Django View  ',
        'Gives u the most control over your application logic',
        'is mapped manually to URLS'

        ]
        return Response({'mesaage':'Hello','an_apiview':an_apiview})

    def post(self,request):
         """ create a hello message with our name """
         serializer=self.serializer_class(data=request.data)

         if serializer.is_valid():
             name=serializer.validated_data.get('name')
             mesaage=f'Hello {name}'
             return Response({'message':mesaage})
         else:
             return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def put(self,request, pk=None):
        """handle UPDATING an object """
        return Response({'method':'PUT'})
    def patch(self,request, pk=None):
        """handle a PARTIAL-UPDATE of an object """
        return Response({'method':'PATCH'})
    def delete(self,request, pk=None):
        """TO DELETE an object """
        return Response({'method':'DELETE'})

#-------------------------------------------------------------------------------
#http://127.0.0.1:8000/api/hello-viewset/
#http://127.0.0.1:8000/api/hello-viewset/1


class HelloViewSet(viewsets.ViewSet):
    """Test Api ViewSets"""

    #serializer using
    serializer_class=serializers.HelloSerializers

    def list(self,request):
        """Returns a List of  ViewSet """
        a_viewset=[
        'Uses HTTPS actions as functions (list,update,partial_update,create, retrieve,destroy)',
        'Automatically maps to router URLS  ',
        'Provides more fuctionality with less code',
        ]
        return Response({'mesaage':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """create a new hello message """
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            mesaage=f'Hello {name}'
            return Response({'message':mesaage})
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """ getting an object by ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ HANDLES updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating part of object """
        return Response({'http_method':'PATCH'})
    def destroy(self,request,pk=None):
        """REMOVE object """
        return Response({'http_method':'DELETE'})

#viewset.ModelViewSet set is similar to simple
#ViewSet specifically manage moels through api
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
#adding permissions
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
#adding search
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')
#-------------------------------------------------------------------------------

class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
#-------------------------------------------------------------------------------
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
#-------------------------------------------------------------------------------
#    permission_classes = (    permissions.UpdateOwnStatus,    IsAuthenticatedOrReadOnly)
#-------------------------------------------------------------------------------
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)
#-------------------------------------------------------------------------------
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
