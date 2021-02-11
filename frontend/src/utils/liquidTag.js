const youtubeReg = /{% youtube (\w+) %}/gi;
const youtubeExp =
  "<iframe style='width:100%; height:500px' src='https://www.youtube.com/embed/$1'></iframe>";
const codesandboxReg = /{% codesandbox (\S+) %}/g;
const codesandboxExp =
  "<iframe src='https://codesandbox.io/embed/$1?fontsize=14&hidenavigation=1&theme=dark?'  style='width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;'  allow='accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking' sandbox='allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts'></iframe>";
const liquidResolver = str => {
  return str
    .replace(youtubeReg, youtubeExp)
    .replace(codesandboxReg, codesandboxExp);
};

export { liquidResolver };
