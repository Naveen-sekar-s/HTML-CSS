//Small understandable code using ifelse
let checkGrade = 49;
let yourGrade;
if (checkGrade >= 90) {
  yourGrade = "A+";
} else if (checkGrade >= 80) {
  yourGrade = "B";
} else if (checkGrade >= 70) {
  yourGrade = "C";
} else if (checkGrade >= 60) {
  yourGrade = "D+";
} else if (checkGrade >= 50) {
  yourGrade = "D";
} else {
  yourGrade = "Say bye to Your life";
}

console.log(yourGrade);
