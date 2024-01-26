export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (false) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error(''));
    }
  });
}

handleResponseFromAPI()
  .then((result) => {
    console.log("Got a response from the API");
    return result;
  })
  .catch((error) => {
    console.error("Error:", error);
  });