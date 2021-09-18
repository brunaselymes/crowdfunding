from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Category, Pledge, Perk
from .serializers import (
    PledgeDetailSerializer,
    ProjectSerializer,
    CategorySerializer,
    PledgeSerializer,
    ProjectDetailSerializer,
    CategoryDetailSerializer,
    PerkSerializer,
    PerkDetailSerializer,
)
from django.http import Http404
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Category.objects.get(pk=pk)
    #     except Category.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     category = self.get_object(pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     category = self.get_object(pk)
    #     serializer = CategoryDetailSerializer(category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     project = self.get_object(pk)
    #     project.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            self.check_object_permissions(self.request, category)
            return category
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PledgeDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pledge = self.get_object(pk)
        serializer = PledgeDetailSerializer(pledge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PerkList(APIView):
    def get(self, request):
        perks = Perk.objects.all()
        serializer = PerkSerializer(perks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            perk = Perk.objects.get(pk=pk)
            self.check_object_permissions(self.request, perk)
            return perk
        except Perk.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        perk = self.get_object(pk)
        serializer = PerkDetailSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        perk = self.get_object(pk)
        serializer = PerkDetailSerializer(perk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        perk = self.get_object(pk)
        perk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
