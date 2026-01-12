from rest_framework import serializers
from .models import Project, Experience, Service, PriseDeContact, SocialNetwork, Location


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "user",
            "resume",
            "title",
            "image",
            "link",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "user",
            "role",
            "nom_entreprise",
            "date_debut",
            "date_fin",
            "description",
            "type_de_contrat",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "user",
            "nom",
            "details",
            "type_de_service",
            "outils",
        ]


class PriseDeContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriseDeContact
        fields = [
            "id",
            "user",
            "nom_complet",
            "objet",
            "email",
            "message",
            "date_creation",
        ]
        read_only_fields = ["date_creation"]


class ReseauSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReseauSocial
        fields = [
            "id",
            "user", 
            "nom_platforme",
            "lien",
        ]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "user",
            "city",
            "country",
            "longitude",
            "latitude",
        ]