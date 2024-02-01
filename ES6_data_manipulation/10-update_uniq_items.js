export default function updateUniqueItems(miMapa) {
  if (!(miMapa instanceof Map)) {
    throw new Error('Cannot process');
  }
  miMapa.forEach((valor, clave) => {
    if (valor === 1) {
      miMapa.set(clave, 100);
    }
    return miMapa;
  });
}
