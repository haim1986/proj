// console.log("conncected");
var restart = document.querySelector('#b');

var squars = document.querySelectorAll('td');

function clearBoard() {
  for (var i = 0; i < squars.length; i++) {
    squars[i].textContent= '';
  }
}

for (var i = 0; i < squars.length; i++) {
  squars[i].addEventListener('click',changeContent)
}

function changeContent(){
  if (this.textContent === ''){
    this.textContent = 'X';
  }
  else if (this.textContent ==='X') {
    this.textContent = 'O';
  }
  else {
    this.textContent = ""
  }
}

restart.addEventListener('click',clearBoard)
