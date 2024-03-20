let value = "";
for (i = 0; i <= 10; i += 1) {
  if (i === 4) {
    continue;
  }
  value += i;
}
console.log(value);
