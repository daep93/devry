export default {
  isLogined(state) {
    return state.id !== '';
  },
  getAccountModal(state) {
    return state.accountModal;
  },
  getAccountModalType(state) {
    return state.accountModalType;
  },
  getAccountId(state) {
    return state.id;
  },
  getAccountNickname(state) {
    return state.nickname;
  },
  getMyTags(state) {
    return state.id !== '' ? ['javascript', 'vue.js', 'python3'] : state.myTags;
  },
  getSelectedTags(state) {
    return state.selectedTags;
  },
};
