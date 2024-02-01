export default function cleanSet(set, startString) {
  if (!startString || !(typeof startString === 'string')) {
    return '';
  }
  const iterator = set.values();
  let strResult = '';
  for (let i = 0; i < set.size; i += 1) {
    const str1 = iterator.next().value;
    if (str1.startsWith(startString)) {
      const longitudPrefijo = startString.length;
      const resultado = str1.substring(longitudPrefijo);
      strResult += `${resultado}-`;
    }
  }
  const strSinGuion = strResult.slice(0, -1);
  return strSinGuion;
}
