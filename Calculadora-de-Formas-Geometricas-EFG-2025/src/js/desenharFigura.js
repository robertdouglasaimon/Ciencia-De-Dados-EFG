// 🎨 desenharFigura.js
function desenharFigura(figura, largura, altura, rotacao = 0, escala = 1) {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#4caf50";

  ctx.save();
  ctx.translate(canvas.width / 2, canvas.height / 2);
  ctx.rotate((rotacao * Math.PI) / 180);
  ctx.scale(escala, escala);

  if (figura === "quadrado") {
    ctx.fillRect(-largura / 2, -largura / 2, largura, largura);
  } else if (figura === "retangulo") {
    ctx.fillRect(-largura / 2, -altura / 2, largura, altura);
  } else if (figura === "triangulo") {
    ctx.beginPath();
    ctx.moveTo(0, -altura / 2);
    ctx.lineTo(-largura / 2, altura / 2);
    ctx.lineTo(largura / 2, altura / 2);
    ctx.closePath();
    ctx.fill();
  } else if (figura === "circulo") {
    const raio = largura / 2;
    ctx.beginPath();
    ctx.arc(0, 0, raio, 0, 2 * Math.PI);
    ctx.fill();
  }

  ctx.restore();
}
