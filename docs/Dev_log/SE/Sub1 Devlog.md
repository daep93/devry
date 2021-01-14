# 2021.01.14 목요일

## 오늘 한 일

- login 로직 구현

  





## 배운점

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

상단의 checkForm 함수를 작성하고 submit 버튼이랑 연결했으나, 이렇게 구현하면 실시간으로 데이터를 감시하며 오류를 표시하는게 불가능하다는 것을 알게됨









