from django.db.models import fields
from rest_framework import serializers
from .models import Project, Category, Pledge


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    # id = serializers.ReadOnlyField()
    # title = serializers.CharField(max_length=200)
    # description = serializers.CharField(max_length=None)
    # image = serializers.URLField()
    # is_active = serializers.BooleanField()
    # goal = serializers.IntegerField()
    # created_date = serializers.DateTimeField()
    # close_date = serializers.DateTimeField()
    # user = serializers.ReadOnlyField(source='user.id')
    # category = serializers.CharField(max_length=200)

    # def create(self, validated_data):
    #     return Project.objects.create(**validated_data)


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    project_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.goal = validated_data.get("goal", instance.goal)
        instance.image = validated_data.get("image", instance.image)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.created_date = validated_data.get(
            "created_date", instance.created_date
        )
        instance.close_date = validated_data.get("close_date", instance.close_date)
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        return instance
