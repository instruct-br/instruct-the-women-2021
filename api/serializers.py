from rest_framework import serializers

from .models import PackageRelease, Project
from .pypi import version_exists, latest_version


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}

    def validate(self, data):
        # TODO
        # Validar o pacote, checar se ele existe na versão especificada.
        # Buscar a última versão caso ela não seja especificada pelo usuário.
        # Subir a exceção `serializers.ValidationError()` se o pacote não
        # for válido.
        return data


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        # TODO
        # Salvar o projeto e seus pacotes associados.
        packages = validated_data["packages"]
        return Project(name=validated_data["name"])
