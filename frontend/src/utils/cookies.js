// function saveAuthToCookie(value) {
//   document.cookie = `til_auth=${value}`;
// }

// function saveUserIdToCookie(value) {
//   document.cookie = `til_user_id=${value}`;
// }
// function saveUserNicknameToCookie(value) {
//   document.cookie = `til_user_nickname=${value}`;
// }

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
    /(?:(?:^|.*;\s*)til_auth\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getUserIdFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)til_user_id\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}
function getUserNicknameFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)til_user_nickname\s*=\s*([^;]*).*$)|^.*$/,
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
