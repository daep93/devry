const testCase = [
  {
    event_id: 1, // 이벤트 게시글 번호
    category: 'conference', // 이벤트 카테고리
    title: 'Vue.js Conference', // 이벤트 제목
    tags: ['vue', 'Conference'], // 이벤트 관련 태그
    date: '2021.03.15', // 이벤트 개최 일자
    host_info: {
      // 이벤트 주최자 정보
      user_id: 1, // 이벤트 주최자 id
      profile_img:
        'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F99E375455D5E2D6A1960E9', // 이벤트 주최자 프로필 이미지
    },
    bookmark: false, // 북마크 여부
  },
  {
    event_id: 2,
    category: 'workshop',
    title: 'JavaScript Workshop',
    tags: ['javaScript', 'Workshop'],
    date: '2021.03.20',
    host_info: {
      user_id: 3,
      profile_img:
        'https://img.etoday.co.kr/pto_db/2019/10/600/20191008190706_1374482_584_432.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 3,
    category: 'hackathon',
    title: 'Bigdata hackathon',
    tags: ['python', 'hackathon'],
    date: '2021.04.20',
    host_info: {
      user_id: 8,
      profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 4,
    category: 'hackathon',
    title: 'AI Speech 해커톤',
    tags: ['AI', 'python', 'hackathon'],
    date: '2021.04.27',
    host_info: {
      user_id: 5,
      profile_img: 'https://cdn.quasar.dev/img/chicken-salad.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 5,
    category: 'conference',
    title: '타입스크립트 컨퍼런스',
    tags: ['typescript', 'conference'],
    date: '2021.03.10',
    host_info: {
      user_id: 6,
      profile_img: 'https://cdn.quasar.dev/img/parallax2.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 6,
    category: 'hackathon',
    title: 'React hackathon',
    tags: ['react', 'hackathon'],
    date: '2021.05.02',
    host_info: {
      user_id: 4,
      profile_img: 'https://cdn.quasar.dev/img/donuts.png',
    },
    bookmark: false,
  },
  {
    event_id: 7,
    category: 'conferendce',
    title: '문화콘텐츠 AI 컨퍼런스',
    tags: ['AI', 'python', 'conferendce'],
    date: '2021.04.18',
    host_info: {
      user_id: 7,
      profile_img: 'https://cdn.quasar.dev/img/linux-avatar.png',
    },
    bookmark: false,
  },
  {
    event_id: 8,
    category: 'workshop',
    title: 'react 워크샵',
    tags: ['react', 'workshop'],
    date: '2021.03.27',
    host_info: {
      user_id: 21,
      profile_img: 'https://cdn.quasar.dev/img/cat.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 9,
    category: 'hackathon',
    title: '제 5회 융합 해커톤',
    tags: ['vue', 'django', 'hackathon'],
    date: '2021.06.13',
    host_info: {
      user_id: 11,
      profile_img: 'https://cdn.quasar.dev/img/material.png',
    },
    bookmark: false,
  },
  {
    event_id: 10,
    category: 'conferendce',
    title: 'Java 컨퍼런스',
    tags: ['java', 'conferendce'],
    date: '2021.04.17',
    host_info: {
      user_id: 13,
      profile_img: 'https://cdn.quasar.dev/img/mountains.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 11,
    category: 'workshop',
    title: 'docker 워크샵',
    tags: ['docker', 'workshop'],
    date: '2021.03.11',
    host_info: {
      user_id: 17,
      profile_img: 'https://cdn.quasar.dev/img/parallax2.jpg',
    },
    bookmark: false,
  },
  {
    event_id: 12,
    category: 'conference',
    title: 'django 컨퍼런스',
    tags: ['django', 'conference'],
    date: '2021.06.13',
    host_info: {
      user_id: 12,
      profile_img: 'https://cdn.quasar.dev/img/parallax1.jpg',
    },
    bookmark: false,
  },
];
export { testCase };
