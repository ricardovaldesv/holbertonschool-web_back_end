export default function getStudentIdsSum(miArray) {
  const newArray = [];

  if (Array.isArray(miArray)) {
    const sum = miArray.reduce((acumulador, elementoActual) => acumulador + elementoActual.id, 0);
    return sum;
  }
  return newArray;
}
