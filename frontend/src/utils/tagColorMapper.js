const colorDict = {
  vue: 'rgba(65,184,131,1)',
  javascript: 'rgba(247,191,51,1)',
  react: 'rgba(54,168,253,1)',
  angular: 'rgba(181,46,49,1)',
  python: 'rgba(69,132,182,1)',
};
function colorMapper(tags) {
  return tags.map(tag => colorDict[tag.toLowerCase()]);
}
export { colorMapper };
