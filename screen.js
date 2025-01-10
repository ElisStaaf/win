export function log(line) {
  const appDiv = document.getElementById('app');
  const div = document.createElement('div');
  div.innerHTML = line;
  appDiv.appendChild(div)
} 