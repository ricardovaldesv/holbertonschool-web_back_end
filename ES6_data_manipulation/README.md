# ES6 data manipulation

# Learning Objectives

At the end of this project, you are expected to understand:

- How to use map, filter and reduce on arrays
- Typed arrays
- The Set, Map, and Weak link data structures

# Tasks:

## Task 0: Basic list of objects
**Objective:** Create a function getListStudents that returns an array of student objects. Each object should have attributes: id (Number), firstName (String), and location (String).

## Task 1: More mapping
**Objective:** Create a function getListStudentIds that returns an array of student IDs from a list of objects. The function uses the map function on the array.

## Task 2: Filter
**Objective:** Create a function getStudentsByLocation that returns an array of student objects located in a specific city. The function uses the filter function on the array.

## Task 3: Reduce
**Objective:** Create a function getStudentIdsSum that returns the sum of all student IDs. The function uses the reduce function on the array.

## Task 4: Combine
**Objective:** Create a function updateStudentGradeByCity that returns an array of students for a specific city with their new grades. It takes a list of students, a city, and new grades as parameters. The function uses filter and map combined.

## Task 5: Typed Arrays
**Objective:** Create a function createInt8TypedArray that returns a new ArrayBuffer with an Int8 value at a specific position. It takes three arguments: length, position, and value. If adding the value is not possible, an error is thrown.

## Task 6: Set data structure
**Objective:** Create a function setFromArray that returns a Set from an array.

## Task 7: More set data structure
**Objective:** Create a function hasValuesFromArray that returns a boolean indicating whether all elements in an array exist within a set.

## Task 8: Clean set
**Objective:** Create a function cleanSet that returns a string of all set values starting with a specific string (startString). It takes a set and a startString as parameters.

## Task 9: Map data structure
**Objective:** Create a function groceriesList that returns a map of groceries with specific items and quantities.

## Task 10: More map data structure
**Objective:** Create a function updateUniqueItems that returns an updated map for items with initial quantity at 1. It accepts a map as an argument and updates quantities to 100 for entries with quantity 1. If updating is not possible, an error is thrown.
