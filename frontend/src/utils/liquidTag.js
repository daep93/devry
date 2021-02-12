const youtubeReg = /{% youtube (\S+) %}/gi;
const youtubeExp =
  "<div class='row justify-center q-pa-sm full-width'><iframe style='width:60%; height:300px' src='https://www.youtube.com/embed/$1'></iframe></div>";
const codesandboxReg = /{% codesandbox (\S+) %}/g;
const codesandboxExp =
  "<div class='row justify-center q-pa-sm full-width'><iframe src='https://codesandbox.io/embed/$1?fontsize=14&hidenavigation=1&theme=dark?'  style='width:60%; height:300px; border:0; border-radius: 4px; overflow:hidden;'  allow='accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking' sandbox='allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts'></iframe></div>";
const liquidResolver = str => {
  return str
    .replace(youtubeReg, youtubeExp)
    .replace(codesandboxReg, codesandboxExp);
};

export { liquidResolver };
