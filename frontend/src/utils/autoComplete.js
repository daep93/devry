// const all_tags = [
//   { tag: 'Python3', active: false },
//   { tag: 'Django', active: false },
//   { tag: 'Java', active: false },
//   { tag: 'Javascript', active: false },
//   { tag: 'Vue.js', active: false },
//   { tag: 'React', active: false },
//   { tag: 'Angular', active: false },
//   { tag: 'Docker', active: false },
//   { tag: 'FrontEnd', active: false },
//   { tag: 'BackEnd', active: false },
//   { tag: 'Typescript', active: false },
//   { tag: 'Spring', active: false },
//   { tag: 'HTML5', active: false },
//   { tag: 'CSS3', active: false },
//   { tag: 'MySQL', active: false },
//   { tag: 'MariaDB', active: false },
//   { tag: 'Node.js', active: false },
// ];
const all_tags = {
  Python3: false,
  Django: false,
  Java: false,
  Javascript: false,
  'Vue.js': false,
  React: false,
  Angular: false,
  Docker: false,
  FrontEnd: false,
  BackEnd: false,
  Typescript: false,
  Spring: false,
  HTML5: false,
  CSS3: false,
  MySQL: false,
  MariaDB: false,
  'Node.js': false,
};
const filtered_tags = str => {
  const tag = str.charAt(0).toUpperCase() + str.slice(1);
  const reg = new RegExp(tag.trim());
  if (str !== '') {
    return Object.keys(all_tags).filter(el => el.match(reg));
  } else return [];
};
export { filtered_tags, all_tags };
