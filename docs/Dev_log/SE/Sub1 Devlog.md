# 2021.01.14 목요일

## 오늘 한 일

- login 로직 구현
- 서버 연결



## 배운점

### computed를 사용하여 의존성 데이터 평가

사용자의 입력을 실시간으로 받고, e-mail, password 각각 해당하는 오류를 띄우고자 했음

**먼저 작성했던 코드**

```javascript
method {
   checkForm(e) {
      e.preventDefault();
      if (!this.email) {
        this.emailErrors.push('이메일은 필수입니다.');
      } else if (!this.validEmail(this.email)) {
        this.emailErrors.push('이메일 형식을 다시 확인해주세요.');
      }
      if (!this.password) {
        this.passwordErrors.push('비밀번호는 필수입니다.');
      }
      if (this.password.length < 6) {
        this.passwordErrors.push('비밀번호는 6글자 이상입니다.');
      } else if (this.password.length > 15) {
        this.passwordErrors.push('비밀번호는 15글자 이하입니다.');
      }
}
```



**문제점**

상단의 checkForm 함수를 작성하고 submit 버튼이랑 연결했으나, 이렇게 구현하면 실시간으로 데이터를 감시하며 오류를 표시하는게 불가능하다는 것을 알게됨 + 매우 비효율적



**수정 결과**

```javascript
<html>
  <q-input
    v-model="password"
	... 중략
    :error="!isValidPwd"   >
    <template v-slot:error>
      <div class="text-red-8" v-if="password.length < 6">
        6자 이상의 비밀번호를 입력해주세요
      </div        
	  <div class="text-red-8" v-else-if="password.length > 12">
        12자 이하의 비밀번호를 입력해주세요
      </div>       <div class="text-red-8" v-else>
        특수문자를 제외하고 입력해주세요
      </div>
    </template>
  </q-input>


<script>
computed: {
    isEmailValid() {
      return this.email === '' || validateEmail(this.email);
    },
    isValidPwd() {
      return this.password === '' || validatePwd(this.password);
    },
    checkForm() {
      console.log(validateEmail(this.email))
      return validateEmail(this.email) && validatePwd(this.password);
    },
  },
</script>
```

computed를 사용하여 데이터 값이 바뀌는 순간마다 검사를 진행하게끔 함



### django - vue 연결







