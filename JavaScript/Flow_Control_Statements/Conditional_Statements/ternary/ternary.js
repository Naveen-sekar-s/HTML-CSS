const marks = 42;
const CollegeStudent = false;
const result =
  marks == 100
    ? "A+"
    : marks >= 95
    ? "A"
    : marks >= 90
    ? "B+"
    : marks >= 85
    ? "B"
    : marks > 75
    ? "C+"
    : marks >= 70
    ? "C"
    : marks >= 65
    ? "D+"
    : marks >= 50
    ? "D"
    : CollegeStudent
    ? "RA"
    : "Do What You Want";
console.log(result);
