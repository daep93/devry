# 2021.01.18 월요일

## 오늘 한 일

- 기획 기반 와이어프레임 제작하기
- 와이어프레임 공유 (10PM)



# 2021.01.19 화요일

## 오늘 한 일

- 팔로잉/팔로워 목록 모달 프로토타입 제작
- 프로필, 회원정보수정 프로토타입 확인 및 피드백 달기
- 로그인 성공/실패 메시지 출력 및 성공시 모달 꺼지는 기능 구현



## 배운점

**이전 코드**

```javascript
methods: {
	//... 중략
    offModal() {
      this.$store.commit('offAccountModal');
    },
    async submitForm() {
      let check = true;
      try {
        this.$q.loading.show();
        await this.$store.dispatch('LOGIN', {
          username: this.email,
          password: this.password,
        },
        alert('로그인 성공'),                  // 문제점 발생 부분
        this.offModal(),
	  );
      } catch (error) {
        check = false;
        console.log(error);
        alert('이메일이나 비밀번호를 다시 확인해주세요.');
      } finally {
        this.$q.loading.hide();
      }
    },
  },
```

로그인 성공시 alert 성공 메시지 출력 및 모달이 꺼지는 함수 작동하게, 로그인 실패시 실패 메시지를 출력하고자 함

올바른 계정 정보를 입력하면 문제가 발생하지 않았으나, 존재하지 않는 계정으로 로그인을 시도할 경우 문제 발생

- [ **로그인 성공** 메시지 출력 `->` offModal 함수 실행 `->` **로그인 실패** 메시지 출력 ] 순서로 실행이 되는 것을 확인함

문제점 발생 이유: try catch문 이해 부족

- try에서 작성된 무든 구문이 먼저 실행된 이후, 에러 발생 시 catch가 실행되는 구조
- try 구문 안에 성공 메시지 및 offModal 함수를 작성했기 때문에, 에러 발생 시에도 위 코드들이 먼저 실행된 이후 에러 메시지를 출력



**수정**

```javascript
  methods: {
	// ... 중략
    offModal() {
      this.$store.commit('offAccountModal');
    },
    async submitForm() {
      let check = true;
      try {
        this.$q.loading.show();
        await this.$store.dispatch('LOGIN', {
          username: this.email,
          password: this.password,
        });
      } catch (error) {
        check = false;
        console.log(error);
        alert('이메일이나 비밀번호를 다시 확인해주세요.');
      } finally {
        this.$q.loading.hide();
      }
      if (check === true) {
        alert('로그인 성공'), this.offModal();      // 추가
      }
    },
  },
```

true, false로 에러 발생여부를 판단하여, 성공시 메시지 출력 및 offModal 함수를 실행시킴



**수정방안 2**

```javascript
methods: {
    fingPwdModal() {
      this.$store.commit('setAccountModalType', 'findPwd');
    },
    offModal() {
      this.$store.commit('offAccountModal');
    },
    async submitForm() {
      try {
        this.$q.loading.show();
        await this.$store.dispatch('LOGIN', {
          username: this.email,
          password: this.password,
        });                                 // 이 부분
        this.$q.loading.hide();
        alert('로그인 성공');
        this.offModal();
      } catch (error) {
        console.log(error);
        this.$q.loading.hide();
        alert('이메일이나 비밀번호를 다시 확인해주세요.');
      }
    },
  },
```

그냥 try문 밖에서 바로 메시지를 출력하면 되는거였음



# 2021.01.20 수요일

## 오늘 한 일

- Follow 모달 페이지 화면 구현
  - 팔로워
  - 팔로잉
- Jira 이슈 등록