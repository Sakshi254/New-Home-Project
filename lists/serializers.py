from rest_framework import serializers
from .models import List
from accounts.models import Account
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
import django_filters


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'

class ListFilters(django_filters.FilterSet):
    state = django_filters.CharFilter(lookup_expr='exact')
    city = django_filters.CharFilter(lookup_expr='exact')
    description = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='lte')
    bedrooms = django_filters.NumberFilter(lookup_expr='gte')
    bathrooms = django_filters.NumberFilter(lookup_expr='gte')
    garage = django_filters.NumberFilter(lookup_expr='gte')
    sqft = django_filters.NumberFilter(lookup_expr='lte')

    class Meta:
        model = List
        fields = ['state','city','description','price','bedrooms','bathrooms','garage','sqft']

class AccountSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Account.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    