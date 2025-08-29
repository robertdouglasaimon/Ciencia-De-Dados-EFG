// 🧮 calculoDasAreas.js 
function calcular() {
  const figura = document.getElementById("figura").value;
  const largura = parseFloat(document.getElementById("largura").value);
  const altura = parseFloat(document.getElementById("altura").value);
  const rotacao = parseFloat(document.getElementById("rotacao").value);
  const escala = parseFloat(document.getElementById("escala").value);

  let area = 0;
  let perimetro = 0;

  switch (figura) {
    case "quadrado":
      area = largura * largura;
      perimetro = 4 * largura;
      break;
    case "retangulo":
      area = largura * altura;
      perimetro = 2 * (largura + altura);
      break;
    case "triangulo":
      area = (largura * altura) / 2;
      perimetro = largura + altura + Math.hypot(largura, altura); // aproximação
      break;
    case "circulo":
      const raio = largura / 2;
      area = Math.PI * Math.pow(raio, 2);
      perimetro = 2 * Math.PI * raio;
      break;
  }
  // ⬇️ Adiciona os listeners para atualizar em tempo real
window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("rotacao").addEventListener("input", calcular);
  document.getElementById("escala").addEventListener("input", calcular);
});


  document.getElementById("resultado").innerText =
    `Área: ${area.toFixed(2)} | Perímetro: ${perimetro.toFixed(2)}`;

  desenharFigura(figura, largura, altura, rotacao, escala);
}
