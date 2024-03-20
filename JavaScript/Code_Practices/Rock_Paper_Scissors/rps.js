let playGame = confirm("Shall We Play Rock, Paper or Scissors ");
if (playGame) {
  playerChoices = prompt("Enter Rock, Paper or Scissors");
  if (playerChoices) {
    let player = playerChoices.trim().toLowerCase();
    if (player === "rock" || player === "paper" || player === "scissors") {
      let botChoices = Math.floor(Math.random() * 3 + 1);
      let botChoice =
        botChoices === 1 ? "rock" : botChoices === 2 ? "paper" : "scissors";

      let result =
        player === botChoice
          ? "Tie Game"
          : player === "rock" && botChoice === "paper"
          ? "I am Win "
          : player === "paper" && botChoice === "scissors"
          ? "I am Win"
          : player === "scissors" && botChoice === "rock"
          ? "I am Win"
          : "You Win";

      alert(result);
      
      let playAgain = confirm("You have guts to play with me Again ??");
      playAgain ? location.reload() : alert("Ok, lets play another sometime.");
    } else {
      alert("Open your eyes clearly and type rock, paper or scissors bro");
    }
  } else {
    alert("I think You have last minutes guts loss problem");
  }
} else {
  alert("If you have guts play with Me !! ");
}
