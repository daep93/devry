function saveAuthToCookie(value) {
  document.cookie = `login_token=${value}`;
}
function saveUserIdToCookie(value) {
  document.cookie = `login_id=${value}`;
}
function saveUserNicknameToCookie(value) {
  document.cookie = `login_nickname=${value}`;
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
function deleteCookie(value) {
  document.cookie = `${value}=; expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}

export {
  saveAuthToCookie,
  saveUserIdToCookie,
  saveUserNicknameToCookie,
  getAuthFromCookie,
  getUserIdFromCookie,
  getUserNicknameFromCookie,
  deleteCookie,
};
