export default function getListStudentIds(miArray) {
  const newArray = [];
  if (Array.isArray(miArray)) {
    for (let i = 0; i < miArray.length; i++) {
      newArray.push(miArray[i].id);
    }
  }
  return newArray;
}
