const testCase = [
  {
    questId: 10, // 질문 글 번호
    title: 'Vue axios 사용법 질문 ', // 글 제목
    writtenTime: '2021-01-25T11:02', // 글 작성 시간
    refTags: ['javascript', 'vue'], // 참조된 태그
    liked: true, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 6, // 좋아요 횟수
    commentNum: 2, // 댓글 갯수
    viewedNum: 14, // 조회 수
    solved: false, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 1, // 유저 구분 가능한 id
      username: 'SSAFY Lee', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 9, // 질문 글 번호
    title: 'React redux 요즘 왜 하향세인가요? ', // 글 제목
    writtenTime: '2021-01-25T03:34', // 글 작성 시간
    refTags: ['javascript', 'react'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 5, // 좋아요 횟수
    commentNum: 2, // 댓글 갯수
    viewedNum: 50, // 조회 수
    solved: true, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY KIM', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 8, // 질문 글 번호
    title:
      'vue 에서 첨부한 이미지와 같이 만드려면 어떠한 정보를 참조하면 좋을까요?', // 글 제목
    writtenTime: '2021-01-25T02:08', // 글 작성 시간
    refTags: ['javascript', 'vue'], // 참조된 태그
    liked: true, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 6, // 좋아요 횟수
    commentNum: 3, // 댓글 갯수
    viewedNum: 74, // 조회 수
    solved: false, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 1, // 유저 구분 가능한 id
      username: 'SSAFY You', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 7, // 질문 글 번호
    title: 'django fs로 파일을 읽은 데이터를 vue로 전달이 안되서 문의 합니다. ', // 글 제목
    writtenTime: '2021-01-25T01:02', // 글 작성 시간
    refTags: ['vue', 'javascript', 'django'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 14, // 좋아요 횟수
    commentNum: 5, // 댓글 갯수
    viewedNum: 30, // 조회 수
    solved: true, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY KIM', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 6, // 질문 글 번호
    title: 'docker 개발환경 구축 질문드립니다', // 글 제목
    writtenTime: '2021-01-24T20:33', // 글 작성 시간
    refTags: ['docker'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 4, // 좋아요 횟수
    commentNum: 5, // 댓글 갯수
    viewedNum: 20, // 조회 수
    solved: true, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY MAN', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 5, // 질문 글 번호
    title: 'React에서 java 함수가 호출이 가능한가요?', // 글 제목
    writtenTime: '2021-01-24T11:16', // 글 작성 시간
    refTags: ['java', 'react'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 2, // 좋아요 횟수
    commentNum: 6, // 댓글 갯수
    viewedNum: 42, // 조회 수
    solved: true, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY KIM', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 4, // 질문 글 번호
    title:
      'flutter 로 구현된 앱에, 코틀린과 objective-c sdk 를 붙일 수 있을까요?', // 글 제목
    writtenTime: '2021-01-24T04:01', // 글 작성 시간
    refTags: ['flutter', 'swift'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 7, // 좋아요 횟수
    commentNum: 2, // 댓글 갯수
    viewedNum: 82, // 조회 수
    solved: false, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY SAY', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 3, // 질문 글 번호
    title: 'python / Django / url 설정 (<str:****)에 관련하여 질문', // 글 제목
    writtenTime: '2021-01-24T02:43', // 글 작성 시간
    refTags: ['python', 'django'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 4, // 좋아요 횟수
    commentNum: 1, // 댓글 갯수
    viewedNum: 70, // 조회 수
    solved: false, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY KIM', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 2, // 질문 글 번호
    title:
      'swift webview와 android webview 차이점이 있나요? 안드로이드에서는 되는데 swift에서는 안될때', // 글 제목
    writtenTime: '2021-01-24T02:22', // 글 작성 시간
    refTags: ['swift'], // 참조된 태그
    liked: false, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 1, // 좋아요 횟수
    commentNum: 4, // 댓글 갯수
    viewedNum: 44, // 조회 수
    solved: true, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY MON', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
  {
    questId: 1, // 질문 글 번호
    title: 'Typescript에서 React 사용할때 getState() 질문', // 글 제목
    writtenTime: '2021-01-24T02:02', // 글 작성 시간
    refTags: ['react', 'typescript'], // 참조된 태그
    liked: true, // 토큰을 넘겨서 인증한 api 요청자가 해당 게시물에 좋아요를 눌렀는지 여부
    likeNum: 16, // 좋아요 횟수
    commentNum: 2, // 댓글 갯수
    viewedNum: 97, // 조회 수
    solved: true, // 질문 해결 여부
    userInfo: {
      // 질문 글 작성자 정보
      userId: 2, // 유저 구분 가능한 id
      username: 'SSAFY MOM', // 닉네임
      profileUrl: '/user/1', // 프로필 사진 url
    },
  },
];
export { testCase };
