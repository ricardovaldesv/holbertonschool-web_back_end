import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const signUpUserPromise = signUpUser(firstName, lastName);
  const uploadPhotoPromise = uploadPhoto(fileName);

  return Promise.allSettled([signUpUserPromise, uploadPhotoPromise])
    .then((results) => results.map((result) => ({
      tatus: result.status,
      value: result.status === 'fulfilled' ? result.value : { error: result.reason },
    })))
    .catch((error) => {
      console.error(error);
      return [];
    });
}
