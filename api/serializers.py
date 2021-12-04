from django.contrib.auth.models import User, Group
from core.models import *
from api.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['firstname', 'lastname', 'address', 'birthday', 'age', 'weight', 'height', 'phone', 'cur', 'rfc', 'sex']

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('name', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.address = validated_data.get('phone', instance.address)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.cur = validated_data.get('cur', instance.cur)
        instance.rfc = validated_data.get('rfc', instance.rfc)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.save()
        return instance


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = ['street', 'city', 'country', 'municipality', 'ext', 'int']

    def create(self, validated_data):
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.municipality = validated_data.get('municipality', instance.municipality)
        instance.cp = validated_data.get('cp', instance.cp)
        instance.ext = validated_data.get('ext', instance.ext)
        instance.int = validated_data.get('int', instance.int)
        instance.save()
        return instance


class MedicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medic
        fields = ['firstname', 'lastname', 'age', 'phone', 'cur', 'rfc', 'sex', 'cedula', 'photo']

    def create(self, validated_data):
        return Medic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.age = validated_data.get('age', instance.age)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.cur = validated_data.get('cur', instance.cur)
        instance.rfc = validated_data.get('rfc', instance.rfc)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.cedula = validated_data.get('cedula', instance.cedula)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


class CiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cite
        fields = ['person', 'medic', 'date']

    def create(self, validated_data):
        return Cite.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.medic = validated_data.get('medic', instance.medic)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['medic', 'person', 'diagnosis', 'date']

    def create(self, validated_data):
        return Diagnosis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.medic = validated_data.get('medic', instance.medic)
        instance.person = validated_data.get('person', instance.person)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class DietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diet
        fields = ['person', 'medic', 'diet', 'date']

    def create(self, validated_data):
        return Diet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.medic = validated_data.get('medic', instance.medic)
        instance.diet = validated_data.get('diet', instance.diet)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = ['person', 'allergy']

    def create(self, validated_data):
        return Allergy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.allergy = validated_data.get('allergy', instance.allergy)
        instance.save()
        return instance


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['person', 'medic', 'diagnosis', 'allergy', 'diet']

    def create(self, validated_data):
        return Record.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.medic = validated_data.get('medic', instance.medic)
        instance.diagnosis = validated_data.get('diagnosis', instance.diagnosis)
        instance.allergy = validated_data.get('allergy', instance.allergy)
        instance.diet = validated_data.get('diet', instance.diet)
        instance.save()
        return instance


class LaboratorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Laboratory
        fields = ['person', 'laboratory', 'date']

    def create(self, validated_data):
        return Laboratory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.person = validated_data.get('person', instance.person)
        instance.laboratory = validated_data.get('laboratory', instance.laboratory)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

