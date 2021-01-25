const colorDict = {
  Vue: 'rgba(65,184,131,0.5)',
  Javascript: 'rgba(247,191,51,0.5)',
  React: 'rgba(54,168,253,0.5)',
  Angular: 'rgba(181,46,49,0.5)',
};
function colorMapper(tags) {
  return tags.map(tag => colorDict[tag]);
}
export { colorMapper };
