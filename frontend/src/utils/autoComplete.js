const tags = [
  'Python3',
  'Django',
  'Java',
  'JavaScript',
  'Vue.js',
  'React',
  'Angular',
  'Docker',
  'FrontEnd',
  'BackEnd',
  'Typescript',
];
const filtered_tags = str => {
  const tag = str.charAt(0).toUpperCase() + str.slice(1);
  const reg = new RegExp(tag.trim());
  if (str !== '') {
    console.log('success');
    return tags.filter(el => el.match(reg));
  } else return [];
};
export { filtered_tags };
