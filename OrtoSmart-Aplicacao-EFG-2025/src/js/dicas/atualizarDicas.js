// Função para atualizar a dica:
function atualizarDica() {
  const dicaAleatoria = window.dicas[Math.floor(Math.random() * window.dicas.length)];
  document.getElementById("dica").innerText = dicaAleatoria;
}

window.onload = function () {
  atualizarDica();
  setInterval(atualizarDica, 10000); // troca a cada 10 segundos
};
