import store from '@/store/state.js';

const filtered_tags = str => {
  const tag = str.charAt(0).toUpperCase() + str.toLowerCase().slice(1);
  const reg = new RegExp(tag.trim());
  if (str !== '') {
    return store.all_tag_list.filter(el => el.match(reg));
  } else return [];
};
export { filtered_tags };
