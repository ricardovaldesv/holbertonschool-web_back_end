export default function getListStudentIds(miArray) {
  const newArray = [];

  if (Array.isArray(miArray)) {
    const newArray = miArray.map((valor) => valor.id);
    return newArray;
  }

  return newArray;
}
