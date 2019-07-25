from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name =  serializers.CharField(max_length=30)
    dob = serializers.CharField(max_length=30)
    sex = serializers.CharField(max_length=30)
    place_of_issue = serializers.CharField(max_length=30)
    Nid = serializers.CharField(max_length=30)
    fprint_data = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

class InsuranceSerializer(serializers.Serializer):
    first_name = serializers.CharField( max_length=30)
    last_name = serializers.CharField(max_length=30)
    dob = serializers.CharField( max_length=20)
    sex = serializers.CharField( max_length=12)
    nid = serializers.CharField( max_length=40)
    policy_no = serializers.CharField( max_length=30)
    card_no = serializers.CharField( max_length=30)
    valid = serializers.CharField( max_length=30)
    patient_contrib = serializers.CharField( max_length=30)
    insurance_compny = serializers.CharField( max_length=30)
class MedicalHistorySerializer(serializers.Serializer):
    chiefComplaint = serializers.CharField()
    pastMedicalHistory = serializers.CharField()
    familyHistory = serializers.CharField()
    drugAndAllergyHistory = serializers.CharField()
    socialHistory = serializers.CharField()
    nid = serializers.CharField(max_length=16)