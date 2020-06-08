from rest_framework import serializers
from .models import Profile,Project,countries,categories,technologies,colors

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields='__all__'

class countriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields='__all__'

class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields='__all__'

class technologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = technologies
        fields='__all__'

class colorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = colors
        fields='__all__'
