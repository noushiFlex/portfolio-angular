from rest_framework import serializers
from .models import Utilisateur
from portfolio.serializer import (
    ProjetSerializer,
    ExperienceSerializer,
    ServiceSerializer,
    ReseauSocialSerializer,
    LocalisationSerializer
)

class UtilisateurSerializer(serializers.ModelSerializer):
    # Utilisation des related_name définis dans les modèles de portfolio.models
    # projets = ProjetSerializer(many=True, read_only=True)
    # experiences = ExperienceSerializer(many=True, read_only=True)
    # services = ServiceSerializer(many=True, read_only=True)
    # reseaux_sociaux = ReseauSocialSerializer(many=True, read_only=True)
    # localisations = LocalisationSerializer(many=True, read_only=True)

    class Meta:
        model = Utilisateur
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'photo_de_profile',
            'description',
            'age',
            'lien_cv',
            'telephone',
            # 'projets',
            # 'experiences',
            # 'services',
            # 'reseaux_sociaux',
            # 'localisations',
        ]