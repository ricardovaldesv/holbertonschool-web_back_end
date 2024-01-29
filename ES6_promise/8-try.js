export default function divideFunction(numerator, denominator) {
  if (numerator && denominator) {
    return numerator / denominator;
  }
  throw Error('cannot divide by 0');
}
