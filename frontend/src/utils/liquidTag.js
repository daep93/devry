const iframeReg1 = /<iframe.*iframe>/gis;
const iframeReg2 = /<iframe.*>/gis;
const iframeExp = '';
const youtubeReg = /{% youtube (\S+) (\S+) (\S+) %}/gi;
const youtubeExp =
  "<div class='row justify-center q-pa-sm full-width'><iframe style='width:$2; height:$3;' src='https://www.youtube.com/embed/$1'></iframe></div>";
const codesandboxReg = /{% codesandbox (\S+) (\S+) (\S+) %}/gi;
const codesandboxExp =
  "<div class='row justify-center q-pa-sm full-width'><iframe src='https://codesandbox.io/embed/$1?fontsize=14&hidenavigation=1&theme=dark?'  style='width:$2; height:$3; border:0; border-radius: 4px; overflow:hidden;'  allow='accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking' sandbox='allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts'></iframe></div>";
const replReg = /{% repl (\S+) (\S+) (\S+) (\S+) %}/gi;
const replExp =
  "<div class='row justify-center q-pa-sm full-width'><iframe frameborder='0' width='$3' height='$4' src='https://repl.it/@$1/$2?lite=true'></iframe> </div>";
const instagramReg = /{% instagram (\S+) (\S+) (\S+) %}/gi;
const instagramExp =
  "<div class='row justify-center q-pa-sm full-width'><iframe width='$2' height='$3' src='https://www.instagram.com/p/$1/embed' frameborder='0'></iframe></div>";
const liquidResolver = str => {
  return str
    .replace(iframeReg1, iframeExp)
    .replace(iframeReg2, iframeExp)
    .replace(youtubeReg, youtubeExp)
    .replace(codesandboxReg, codesandboxExp)
    .replace(replReg, replExp)
    .replace(instagramReg, instagramExp);
};

export { liquidResolver };
