export default function updateStudentGradeByCity(miArray, city, newGrades) {
  const newArray = [];

  if (Array.isArray(miArray)) {
    const newArray1 = miArray.filter((valor) => valor.location === city);
    const newArray2 = newArray1.map((valor) => {
    console.log(valor);
    // const studentId2 = valor.id;
    //console.log(newGrades[0].studentId);
    const obj2 = newGrades.find(obj => obj.studentId === valor.id);
    console.log(obj2);
    valor.grade = obj2.grade;
    console.log(valor);
    return newArray;
  })
  }

  return newArray;
}
