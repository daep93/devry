const colorDict = alpha => {
  return {
    frontend: `rgba(234,78,40,${alpha})`,
    backend: `rgba(86,197,246,${alpha})`,
    angular: `rgba(169,2,42,${alpha})`,
    django: `rgba(16,62,46,${alpha})`,
    java: `rgba(255,143,143,${alpha})`,
    'vue.js': `rgba(65,184,131,${alpha})`,
    typescript: `rgba(49,120,198,${alpha})`,
    docker: `rgba(19,72,113,${alpha})`,
    python3: `rgba(30,56,187,${alpha})`,
    react: `rgba(97,218,246,${alpha})`,
    javascript: `rgba(247,223,30,${alpha})`,
    spring: `rgba(108,179,62,${alpha})`,
    html5: `rgba(239,96,38,${alpha})`,
    css3: `rgba(37,161,225,${alpha})`,
    mysql: `rgba(0,97,139,${alpha})`,
    mariadb: `rgba(196,154,108,${alpha})`,
    'node.js': `rgba(128,189,1,${alpha})`,
  };
};
const matchingColorDict = alpha => {
  return {
    frontend: '#ffffff',
    backend: `rgba(43,58,72,${alpha})`,
    angular: '#ffffff',
    django: '#ffffff',
    java: `rgba(1,71,110,${alpha})`,
    'vue.js': `rgba(53,73,94,${alpha})`,
    typescript: '#ffffff',
    docker: `rgba(115,199,230,${alpha})`,
    python3: `rgba(255,223,91,${alpha})`,
    react: `rgba(34,34,34,${alpha})`,
    javascript: '#000000',
    spring: '#ffffff',
    html5: '#ffffff',
    css3: '#000000',
    mysql: `rgba(229,142,0,${alpha})`,
    mariadb: `rgba(0,42,99,${alpha})`,
    'node.js': `rgba(0,42,99,${alpha})`,
  };
};

function colorListMapper(tags, alpha) {
  return tags.map(tag => colorDict(alpha)[tag.toLowerCase()]);
}
function colorSoloMapper(tag, alpha) {
  return colorDict(alpha)[tag.toLowerCase()];
}
function matchingColorSoloMapper(tag, alpha) {
  return matchingColorDict(alpha)[tag.toLowerCase()];
}
export { colorListMapper, colorSoloMapper, matchingColorSoloMapper };
