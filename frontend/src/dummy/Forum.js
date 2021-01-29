const testCase = [
  {
    forum_id: 1, // 포럼 글 번호
    title: 'Add a YouTube stats widget to your iPhone with JavaScript', // 글 제목
    thumnail:
      'https://techcrunch.com/wp-content/uploads/2019/10/youtube-ios-app.jpg?w=1024', // 글의 썸네일 이미지
    ref_tags: ['vue', 'javascript'], // 참조된 태그
    like_num: 7, // 글 좋아요 갯수
    like_status: true, // 현재 로그인한 유저의 해당 글에 대한 좋아요 상태 표시
    comment_num: 1, // 댓글 갯수
    viewed_num: 20, // 조회 수
    bookmark_status: false, // 글의 북마크 여부 표시
    user_info: {
      // 글 작성자 정보
      user_id: 3, // 유저 구분 가능한 id
      username: 'test1', // 유저 닉네임
      written_time: '2021-01-24T02:01', // 글 작성 시간
      profile_img: 'https://cdn.quasar.dev/img/avatar.png', // 글 작성자의 프로필 이미지
    },
  },
  {
    forum_id: 2,
    title: 'Git Merge Request 관련하여',
    thumnail:
      'https://cdn.shortpixel.ai/client/q_glossy,ret_img,w_796,h_448/https://techuncode.com/wp-content/uploads/2020/09/what-is-a-computer-algorithm.jpg',
    ref_tags: ['Git'],
    like_num: 10,
    like_status: true,
    comment_num: 3,
    viewed_num: 10,
    bookmark_status: false,
    user_info: {
      // 글 작성자 정보
      user_id: 5,
      username: '코린이',
      written_time: '2021-01-27T03:04',
      profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
    },
  },
  {
    forum_id: 3,
    title: 'Add a YouTube stats widget to your iPhone with JavaScript',
    thumnail:
      'https://www.simplilearn.com/ice9/free_resources_article_thumb/Best-Programming-Languages-to-Start-Learning-Today.jpg',
    ref_tags: ['vue', 'javascript', 'frontend'],
    like_num: 20,
    like_status: false,
    comment_num: 3,
    viewed_num: 50,
    bookmark_status: false,
    user_info: {
      // 글 작성자 정보
      user_id: 4,
      username: 'mark',
      written_time: '2021-01-25T04:09',
      profile_img:
        'https://www.impel.eu/wp-content/uploads/2019/08/mediterranean-sea.jpg',
    },
  },
  {
    forum_id: 4,
    title: 'JPA 정적인 테이블들 관리법 팁',
    thumnail:
      'https://i1.wp.com/www.thistechnologylife.com/wp-content/uploads/2020/07/JPA.png?fit=839%2C278',
    ref_tags: ['java', 'spring'],
    like_num: 7,
    like_status: false,
    comment_num: 2,
    viewed_num: 20,
    bookmark_status: false,
    user_info: {
      // 글 작성자 정보
      user_id: 7,
      username: 'sarah',
      written_time: '2021-01-23T05:12',
      profile_img:
        'https://www.adorama.com/alc/wp-content/uploads/2017/11/shutterstock_114802408.jpg',
    },
  },
  {
    forum_id: 5,
    title: 'React 불필요한 렌더링을 막는 방법',
    thumnail: 'https://miro.medium.com/max/3200/1*qXcjSfRj0C0ir2yMsYiRyw.jpeg',
    ref_tags: ['react', 'frontend'],
    like_num: 8,
    like_status: true,
    comment_num: 2,
    viewed_num: 27,
    bookmark_status: false,
    user_info: {
      // 글 작성자 정보
      user_id: 10,
      username: 'james',
      written_time: '2021-01-21T03:02',
      profile_img: 'https://news.gsu.edu/files/2020/11/milky-way.jpg',
    },
  },
  {
    forum_id: 6,
    title: '프론트엔드 성능 점검 항목 – 2021 버전',
    thumnail: 'https://miro.medium.com/max/820/1*Y4Td-XMRtuFAW_8CpO7KyA.png',
    ref_tags: ['frontend', 'javascript', 'typescript'],
    like_num: 15,
    like_status: false,
    comment_num: 9,
    viewed_num: 60,
    bookmark_status: true,
    user_info: {
      // 글 작성자 정보
      user_id: 12,
      username: 'fe-master',
      written_time: '2021-01-26T05:02',
      profile_img:
        'https://9b16f79ca967fd0708d1-2713572fef44aa49ec323e813b06d2d9.ssl.cf2.rackcdn.com/1140x_a10-7_cTC/20200413dsCalmBeforeStormLocal01-1601476874.jpg',
    },
  },
  {
    forum_id: 7,
    title: 'React 시작할 때 참고하기 좋은 사이트',
    thumnail:
      'https://wonderfulengineering.com/wp-content/uploads/2016/02/wallpaper-background-2.jpg',
    ref_tags: ['frontend', 'javascript', 'react'],
    like_num: 17,
    like_status: true,
    comment_num: 6,
    viewed_num: 35,
    bookmark_status: true,
    user_info: {
      // 글 작성자 정보
      user_id: 13,
      username: 'olive',
      written_time: '2020-12-26T11:02',
      profile_img:
        'https://cdn.pixabay.com/photo/2015/03/26/09/47/sky-690293__340.jpg',
    },
  },
  {
    forum_id: 8,
    title: 'java 8에서 달라진 점',
    thumnail:
      'https://www.simplilearn.com/ice9/free_resources_article_thumb/How_to_Become_a_Back_End_Developer.jpg',
    ref_tags: ['java', 'backend'],
    like_num: 20,
    like_status: false,
    comment_num: 12,
    viewed_num: 63,
    bookmark_status: false,
    user_info: {
      // 글 작성자 정보
      user_id: 14,
      username: 'apple',
      written_time: '2020-07-11T11:56',
      profile_img:
        'https://picjumbo.com/wp-content/uploads/the-golden-gate-bridge-sunset-1080x720.jpg',
    },
  },
  {
    forum_id: 9,
    title: 'Windows 10 에서 redis 설치하기',
    thumnail: 'https://miro.medium.com/max/4000/1*77Vo1RFQ-5DcLKdeHbb2-A.png',
    ref_tags: ['redis', 'database', 'windows', 'cache'],
    like_num: 21,
    like_status: true,
    comment_num: 6,
    viewed_num: 66,
    bookmark_status: false,
    user_info: {
      // 글 작성자 정보
      user_id: 10,
      username: 'james',
      written_time: '2020-09-22T5:56',
      profile_img:
        'https://images.unsplash.com/photo-1490730141103-6cac27aaab94?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8ZnJlZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80',
    },
  },
  {
    forum_id: 10,
    title: 'migration 오류 케이스 정리',
    thumnail:
      'https://upload.wikimedia.org/wikipedia/commons/f/f2/DVD_Rental_Query.png',
    ref_tags: ['database', 'django', 'backend', 'python'],
    like_num: 13,
    like_status: true,
    comment_num: 6,
    viewed_num: 66,
    bookmark_status: true,
    user_info: {
      // 글 작성자 정보
      user_id: 14,
      username: 'apple',
      written_time: '2020-12-22T8:12',
      profile_img:
        'https://thumbs.dreamstime.com/t/%CE%B5%CF%80%CE%AF%CE%BA-%CE%B7%CF%83%CE%B7-%CE%B3%CF%85%CE%BD%CE%B1%CE%B9%CE%BA%CF%8E%CE%BD-%CE%BA%CE%B1%CE%B9-%CE%B5-%CE%B5%CF%8D%CE%B8%CE%B5%CF%81%CE%BF-%CF%80%CE%BF%CF%85-%CE%AF-%CF%80%CE%BF%CF%85-%CE%B1%CF%80%CE%BF-%CE%B1%CE%BC%CE%B2%CE%AC%CE%BD%CE%BF%CF%85%CE%BD-%CF%84%CE%B7-%CF%86%CF%8D%CF%83%CE%B7-%CF%83%CF%84%CE%BF-94227839.jpg',
    },
  },
];
export { testCase };
