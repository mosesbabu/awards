from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import categories,technologies,colors,countries,Project,Profile,Rating
from .forms import ProjectForm,ProfileForm,RatingForm
from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Q
from django.db.models import Max
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer,technologiesSerializer,colorsSerializer,countriesSerializer,categoriesSerializer


# Create your views here.
def index(request):
    date = dt.date.today()
    winners=Project.objects.all()[:4]
    caraousel = Project.objects.order_by('-overall_score')[0]
    nominees=Project.objects.all()[4:8]
    directories=Project.objects.all()[8:11]
    resources=Project.objects.all()[11:15]
    resources2=Project.objects.all()[15:19]

    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(username=current_user)
        print(current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date,"nominees":nominees,"directories":directories,"resources":resources,"resources2":resources2})

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('Index')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.avatar = profile.avatar
            project.country = profile.country

            project.save()
    else:
        form = ProjectForm()

    return render(request,'new_project.html',{"form":form})

def directory(request):
    date = dt.date.today()
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    winners=Project.objects.all()
    caraousel = Project.objects.get(id=8)

    return render(request,'directory.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    projects=Project.objects.filter(username=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

@login_required(login_url='/accounts/login/')
def site(request,site_id):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    try:
        project = Project.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()

    try:
        ratings = Rating.objects.filter(project_id=site_id)
        design = Rating.objects.filter(project_id=site_id).values_list('design',flat=True)
        usability = Rating.objects.filter(project_id=site_id).values_list('usability',flat=True)
        creativity = Rating.objects.filter(project_id=site_id).values_list('creativity',flat=True)
        content = Rating.objects.filter(project_id=site_id).values_list('content',flat=True)
        total_design=0
        total_usability=0
        total_creativity=0
        total_content = 0
        print(design)
        for rate in design:
            total_design+=rate
        print(total_design)

        for rate in usability:
            total_usability+=rate
        print(total_usability)

        for rate in creativity:
            total_creativity+=rate
        print(total_creativity)

        for rate in content:
            total_content+=rate
        print(total_content)

        overall_score=(total_design+total_content+total_usability+total_creativity)/4

        print(overall_score)

        project.design = total_design
        project.usability = total_usability
        project.creativity = total_creativity
        project.content = total_content
        project.overall_score = overall_score

        project.save()

    except:
        return None

    if request.method =='POST':
        form = RatingForm(request.POST,request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project= project
            rating.profile = profile
            rating.overall_score = (rating.design+rating.usability+rating.creativity+rating.content)/2
            rating.save()
    else:
        form = RatingForm()

    return render(request,"site.html",{"project":project,"profile":profile,"ratings":ratings,"form":form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message=f"{search_term}"

        print(searched_projects)

        return render(request,'search.html',{"message":message,"projects":searched_projects,"profile":profile})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def user_profile(request,username):
    user = User.objects.get(username=username)
    profile =Profile.objects.get(username=user)
    projects=Project.objects.filter(username=user)

    return render(request,'user-profile.html',{"projects":projects,"profile":profile})



class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class categoriesList(APIView):
    def get(self, request, format=None):
        all_categories = categories.objects.all()
        serializers = categoriesSerializer(all_categories, many=True)
        return Response(serializers.data)

class technologiesList(APIView):
    def get(self, request, format=None):
        all_technologies = technologies.objects.all()
        serializers = technologiesSerializer(all_technologies, many=True)
        return Response(serializers.data)

class colorsList(APIView):
    def get(self, request, format=None):
        all_colors = colors.objects.all()
        serializers = colorsSerializer(all_colors, many=True)
        return Response(serializers.data)

class countriesList(APIView):
    def get(self, request, format=None):
        all_countries = countries.objects.all()
        serializers = countriesSerializer(all_countries, many=True)
        return Response(serializers.data)
