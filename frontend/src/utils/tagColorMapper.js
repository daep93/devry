function colorMapper(tags, alpha) {
  const colorDict = {
    vue: `rgba(65,184,131,${alpha})`,
    javascript: `rgba(247,191,51,${alpha})`,
    react: `rgba(54,168,253,${alpha})`,
    angular: `rgba(181,46,49,${alpha})`,
    python: `rgba(69,132,182,${alpha})`,
  };
  return tags.map(tag => colorDict[tag.toLowerCase()]);
}
function colorSoloMapper(tag, alpha) {
  const colorDict = {
    vue: `rgba(65,184,131,${alpha})`,
    javascript: `rgba(247,191,51,${alpha})`,
    react: `rgba(54,168,253,${alpha})`,
    angular: `rgba(181,46,49,${alpha})`,
    python: `rgba(69,132,182,${alpha})`,
  };
  return colorDict[tag.toLowerCase()];
}
export { colorMapper, colorSoloMapper };
