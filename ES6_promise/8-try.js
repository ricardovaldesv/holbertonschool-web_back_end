export default function divideFunction(numerator, denominator) {
  if (numerator && denominator) {
    return numerator / denominator;
  }
  return new Error('cannot divide by 0');
}
