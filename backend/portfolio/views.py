from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema 
from .models import Projet, Experience, Service, PriseDeContact, ReseauSocial, Localisation
from .serializer import (
    ProjetSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    PriseDeContactSerializer,
    ReseauSocialSerializer,
    LocalisationSerializer,
)


# Projet Views
@extend_schema(tags=['Projets'])
class ProjetListView(generics.ListAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Projets'])
class ProjetCreateView(generics.CreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Projets'])
class ProjetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = [permissions.AllowAny]


# Experience Views
@extend_schema(tags=['Expériences'])
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Expériences'])
class ExperienceCreateView(generics.CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Expériences'])
class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [permissions.AllowAny]


# Service Views
@extend_schema(tags=['Services'])
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Services'])
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Services'])
class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]


# PriseDeContact Views
@extend_schema(tags=['Contacts'])
class PriseDeContactListView(generics.ListAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Contacts'])
class PriseDeContactCreateView(generics.CreateAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Contacts'])
class PriseDeContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriseDeContact.objects.all()
    serializer_class = PriseDeContactSerializer
    permission_classes = [permissions.AllowAny]


# ReseauSocial Views
@extend_schema(tags=['Réseaux Sociaux'])
class ReseauSocialListView(generics.ListAPIView):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Réseaux Sociaux'])
class ReseauSocialCreateView(generics.CreateAPIView):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Réseaux Sociaux'])
class ReseauSocialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReseauSocial.objects.all()
    serializer_class = ReseauSocialSerializer
    permission_classes = [permissions.AllowAny]


# Localisation Views
@extend_schema(tags=['Localisation'])
class LocalisationListView(generics.ListAPIView):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Localisation'])
class LocalisationCreateView(generics.CreateAPIView):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [permissions.AllowAny]


@extend_schema(tags=['Localisation'])
class LocalisationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localisation.objects.all()
    serializer_class = LocalisationSerializer
    permission_classes = [permissions.AllowAny]




