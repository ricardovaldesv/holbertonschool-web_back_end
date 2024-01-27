import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {};
  const promise2 = {};

  try {
    promise1.value = await signUpUser(firstName, lastName);
    promise1.status = 'fulfilled';
  } catch (err) {
    promise1.value = err.toString();
    promise1.status = 'rejected';
  }

  try {
    promise2.value = await uploadPhoto(fileName);
    promise2.status = 'fulfilled';
  } catch (err) {
    promise2.value = err.toString();
    promise2.status = 'rejected';
  }

  return [promise1, promise2];
}

export default handleProfileSignup;
