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
};
