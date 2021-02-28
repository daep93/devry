from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['email','username','password']
        
        # post나 put과 같이 데이터를 쓰는 것은 가능하나, 조회는 불가능하게 설정
        extra_kwargs ={
            'password' : {'write_only':True}
        }
    
    # 검증 과정은 프론트엔드에서 하기 때문에 생략
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        # 비밀번호를 암호화해서 저장하기 위해 반드시 set_password 사용할 것
        user.set_password(self.validated_data['password'])
        user.save()

class UserLoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['email','password']
        
        # post나 put과 같이 데이터를 쓰는 것은 가능하나, 조회는 불가능하게 설정
        extra_kwargs ={
            'password' : {'write_only':True}
        }