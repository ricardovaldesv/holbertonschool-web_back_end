export default function getStudentsByLocation(miArray, city) {
  const newArray = [];

  if (Array.isArray(miArray)) {
    const newArray = miArray.filter((valor) => valor.location === city);
    return newArray;
  }

  return newArray;
}
