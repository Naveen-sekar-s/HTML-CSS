//if the condition is true if block is executed otherwise else block is executed
let Enter_amount = 400;
let balance = 4000;
if (balance >= Enter_amount) {
  let remain = Enter_amount - balance;
  console.log(`${Enter_amount} Withdrawl Successfully`);
  console.log(`Balance${remain} `);
} else {
  console.log("Inusufficient Balance");
}
