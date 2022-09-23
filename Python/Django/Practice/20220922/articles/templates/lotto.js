
const ball = document.querySelector('.ball')
const number = ball.innerText

switch (Math.floor(number/ 10)) {
  case 0:
    ball.style.backgroundColor = '#d9d90d';
    break
  case 1:
    ball.style.backgroundColor = '#2570e8';
    break
  case 2:
    ball.style.backgroundColor = '#e03636';
  break
  case 3:
    ball.style.backgroundColor = '#707070';
  break
  case 4:
    ball.style.backgroundColor = '#1ed106';
  break
}