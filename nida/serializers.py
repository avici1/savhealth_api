from rest_framework import serializers
from .models import current_status, person


class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    dob = serializers.CharField(max_length=30)
    sex = serializers.CharField(max_length=30)
    place_of_issue = serializers.CharField(max_length=30)
    Nid = serializers.CharField(max_length=30)
    fprint_data = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return person.objects.create(**validated_data)


class InsuranceSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    dob = serializers.CharField(max_length=20)
    sex = serializers.CharField(max_length=12)
    nid = serializers.CharField(max_length=40)
    policy_no = serializers.CharField(max_length=30)
    card_no = serializers.CharField(max_length=30)
    valid = serializers.CharField(max_length=30)
    patient_contrib = serializers.CharField(max_length=30)
    insurance_compny = serializers.CharField(max_length=30)


class MedicalHistorySerializer(serializers.Serializer):
    chiefComplaint = serializers.CharField()
    pastMedicalHistory = serializers.CharField()
    familyHistory = serializers.CharField()
    drugAndAllergyHistory = serializers.CharField()
    socialHistory = serializers.CharField()
    nid = serializers.CharField(max_length=16)


class HospitalSerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    hospitals_name = serializers.CharField(max_length=50)
    speciality = serializers.CharField(max_length=40)
    availability_status = serializers.CharField(max_length=40)
    ho_id = serializers.CharField(max_length=40)


class CurrentStatusSerializer(serializers.Serializer):
    nid = serializers.CharField(max_length=30)
    additional_info = serializers.CharField(max_length=300)
    type_of_injury = serializers.CharField(max_length=300)
    drug_provided = serializers.CharField(max_length=300)
    glasgow_coma_scale = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return current_status.objects.create(**validated_data)
