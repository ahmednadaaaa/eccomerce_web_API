from rest_framework import serializers
from django.contrib.auth.models import User


class SingUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'password')

        extra_kwargs = { #علشان اعمل الصلحيات
            'first_name': {'required':True ,'allow_blank':False}, # required':True يعني مهمه
            'last_name' : {'required':True ,'allow_blank':False},#'allow_blank':False مينفعش يسبها فارغه
            'email' : {'required':True ,'allow_blank':False},
            'password' : {'required':True ,'allow_blank':False,'min_length':8}
        }



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name', 'email', 'username')