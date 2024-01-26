# ES6 Promises

## Learning Objectives

At the end of this project, you are expected to understand:

- Promises and their usage
- Methods like `then`, `resolve`, and `catch`
- Promise object methods
- Handling errors with `throw` and `try`
- The `await` operator
- Usage of async functions

## Tasks

### Task 0: Promise Basics
Return a Promise using the `getResponseFromAPI()` function.

### Task 1: Handling Success and Failure
Return a promise using `getFullResponseFromAPI(success)`. Resolve with status 200 and 'Success' for true, reject with an error for false.

### Task 2: Handling Promises
Create a function `handleResponseFromAPI(promise)` to append handlers to a given promise.

### Task 3: Handling Multiple Promises
Use promises returned from `uploadPhoto` and `createUser` to collectively resolve and log data.

### Task 4: Simple Promise
Return a resolved promise with an object containing first and last names.

### Task 5: Rejecting Promises
Write a function `uploadPhoto(filename)` returning a Promise rejecting with an error.

### Task 6: Handling Multiple Promises Again
Import functions, `signUpUser` and `uploadPhoto`, and create `handleProfileSignup` to handle multiple promises.

### Task 7: Load Balancer
Write a function `loadBalancer(chinaDownload, USDownload)` returning the value of the first resolved promise.

### Task 8: Throwing Errors
Write a function `divideFunction(numerator, denominator)` that throws an error for division by 0.

### Task 9: Try and Catch
Write a function `guardrail(mathFunction)` that appends values or errors to an array, along with the message 'Guardrail was processed'.
