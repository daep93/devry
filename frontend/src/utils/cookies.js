function saveAuthToCookie(value) {
  document.cookie = `login_token=${value}`;
}
function saveUserIdToCookie(value) {
  document.cookie = `login_id=${value}`;
}
function saveUserNicknameToCookie(value) {
  document.cookie = `login_nickname=${value}`;
}
function saveUserMyTagsToCookie(value) {
  // 배열을 쉼표로 구분할 수 있게 합쳐놓을 거임
  document.cookie = `login_my_tags=${value.join(',')}`;
}

function getAuthFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)login_token\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getUserIdFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)login_id\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}
function getUserNicknameFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)login_nickname\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}
function getUserMyTagsFromCookie() {
  //,표로 구분한 데이터를 배열로 분리시킬 거임
  const res = document.cookie.replace(
    /(?:(?:^|.*;\s*)login_my_tags\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
  return res ? res.split(',') : [];
}
function deleteCookie(value) {
  document.cookie = `${value}=; expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}

export {
  saveAuthToCookie,
  saveUserIdToCookie,
  saveUserNicknameToCookie,
  saveUserMyTagsToCookie,
  getAuthFromCookie,
  getUserIdFromCookie,
  getUserNicknameFromCookie,
  getUserMyTagsFromCookie,
  deleteCookie,
};
