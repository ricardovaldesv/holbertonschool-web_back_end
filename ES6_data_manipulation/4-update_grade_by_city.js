export default function updateStudentGradeByCity(miArray, city, newGrades) {
  const newArray1 = miArray.filter((valor) => valor.location === city);
  const newArray2 = newArray1.map((valor) => {
    const updatedValor = { ...valor };
    const obj2 = newGrades.find((obj) => obj.studentId === valor.id);
    if (obj2) {
      updatedValor.grade = obj2.grade;
    } else {
      updatedValor.grade = 'N/A';
    }
    return updatedValor;
  });
  return newArray2;
}
