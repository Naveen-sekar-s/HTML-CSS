/* A string that identifies character or characters to use in separating the string. 
If omitted, a single-element array containing the entire string is returned.
A value used to limit the number of elements returned in the array. */
let str = "Development";
clg = str.split("e", 4); //[ 'D', 'v', 'lopm', 'nt' ]
console.log(clg);
