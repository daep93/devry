export default {
  onAccountModal(state) {
    state.accountModal = true;
  },
  offAccountModal(state) {
    state.accountModal = false;
  },
  onFollowModal(state) {
    state.followModal = true;
  },
  offFollowModal(state) {
    state.followModal = false;
  },
  setAccountModalType(state, type) {
    state.accountModalType = type;
  },
  setUserid(state, id) {
    state.id = id;
  },
  setUsername(state, nickname) {
    state.nickname = nickname;
  },
  setToken(state, token) {
    state.token = token;
  },
  setPassword(state, password) {
    state.password = password;
  },
  clearUserInfo(state) {
    state.id = '';
    state.nickname = '';
    state.token = '';
  },
  toggleLeft(state) {
    state.leftDrawal = !state.leftDrawal;
  },
};
