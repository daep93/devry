import store from '@/store/state.js';

const filtered_tags = str => {
  if (str !== '') {
    const reg = new RegExp(`^${str}`, 'gi');
    return store.all_tag_list.filter(tag => tag.match(reg));
  } else return [];
};
const first_matched_tag = str => {
  const reg = new RegExp(`^${str}`, 'i');
  return store.all_tag_list.find(tag => tag.match(reg));
};
export { filtered_tags, first_matched_tag };
