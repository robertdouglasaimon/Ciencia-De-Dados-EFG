// Variáveis globais
let atual = 0;
let respondidas = 0;
let corretas = 0;
let iniciados = 1;
let completos = 0;

const graficosCirculares = {}; // Armazena os gráficos por ID

// Função para carregar a próxima questão:
function carregarQuestao() {
  const q = questoes[atual];

  // Atualiza o título da questão
  document.getElementById("titulo-questao").innerText = `Questão ${atual + 1} — ${q.tema}`;

  // Remove referência anterior, se existir
  const referenciaAntiga = document.querySelector(".referencia");
  if (referenciaAntiga) {
    referenciaAntiga.remove();
  }

  // Cria e insere a nova referência
  const referencia = document.createElement("p");
  referencia.className = "referencia";
  referencia.innerText = `📚 Banca: ${q.banca || "—"} | Ano: ${q.ano || "—"}`;

  const titulo = document.getElementById("titulo-questao");
  titulo.insertAdjacentElement("afterend", referencia);

  // Atualiza o enunciado
  document.getElementById("enunciado").innerText = q.enunciado;

  // Limpa e monta as alternativas
  const quiz = document.getElementById("quiz");
  quiz.innerHTML = "";

  q.alternativas.forEach((alt, i) => {
    const label = document.createElement("label");
    label.innerHTML = `<input type="radio" name="resposta" value="${i}"> ${alt}`;
    quiz.appendChild(label);
  });
}

// Função para corrigir a resposta:
function corrigir() {
  const resposta = document.querySelector('input[name="resposta"]:checked');
  if (!resposta) return alert("Escolha uma alternativa!");

  respondidas++;
  const q = questoes[atual];
  const correta = parseInt(resposta.value) === q.correta;
  if (correta) corretas++;

  document.getElementById("feedback").innerText = correta
      ? "✅ Correta! " + q.comentario
    : "❌ Errada. " + q.comentario;

  atualizarPainel();

  atual++;
  if (atual < questoes.length) {
    setTimeout(() => {
      document.getElementById("feedback").innerText = "";
      carregarQuestao();
    }, 4000);
  } else {
    completos++;
    alert("Simulado finalizado!");
  }
}

// Função para atualizar o painel:
function atualizarPainel() {
  const rendimento = Math.round((corretas / respondidas) * 100);
  document.getElementById("rendimento").innerText = `${rendimento}%`;
  document.getElementById("respondidas").innerText = respondidas;
  document.getElementById("corretas").innerText = corretas;
  document.getElementById("erros").innerText = respondidas - corretas;
  document.getElementById("iniciados").innerText = iniciados;
  document.getElementById("completos").innerText = completos;

  // Atualiza progresso por tema
  const tema = questoes[atual]?.tema;
  const idProgresso = {
    "Ortografia Geral": "prog-ortografia-geral",
    "Ortografia": "prog-ortografia",
    "Uso de Hífen": "prog-hifen",
    "Acentuação": "prog-acentuacao",
    "Pronomes": "prog-pronomes",
    "Figuras de Linguagem": "prog-figuras",
    "Sintaxe": "prog-sintaxe",
    "Concordância Verbal": "prog-concordancia-verbal",
    "Concordância Nominal": "prog-concordancia-nominal",
    "Regência Verbal": "prog-regencia",
    "Crase": "prog-crase",
    "Pontuação": "prog-pontuacao",
    "Interpretação de Texto": "prog-interpretacao",
    "Semântica": "prog-semantica",
    "Coesão e Coerência": "prog-coesao",
    "Colocação Pronominal": "prog-colocacao",
    "Redação Oficial": "prog-redacao",
    "Fonologia": "prog-fonologia",
    "Morfologia": "prog-morfologia",
    "Vocabulário": "prog-vocabulario",
    "Análise Sintática": "prog-analise-sintatica"
  };


  const id = idProgresso[tema];
  if (id) {
    const barra = document.getElementById(id);
    if (barra) {
      barra.value++;

      // Atualiza gráfico circular no mobile
      const canvasId = id.replace("prog-", "grafico-");
      const canvas = document.getElementById(canvasId);
      if (canvas) {
        const valorAtual = barra.value;
        const maximo = parseInt(barra.max);
        gerarGraficoCircular(canvasId, valorAtual, maximo);
      }

      // Atualiza porcentagem no modo desktop
      const spanId = id.replace("prog-", "porcentagem-");
      const porcentagemSpan = document.getElementById(spanId);
      if (porcentagemSpan) {
        const valorAtual = barra.value;
        const maximo = parseInt(barra.max);
        const porcentagem = Math.round((valorAtual / maximo) * 100);
        porcentagemSpan.innerText = `${porcentagem}%`;
      }
    }
  }
}

// Função para gerar gráficos circulares dos temas em mobile:
function gerarGraficoCircular(idCanvas, valor, maximo) {
  const canvas = document.getElementById(idCanvas);

  if (!canvas) return;

  if (graficosCirculares[idCanvas]) {
    // Atualiza dados do gráfico existente
    const grafico = graficosCirculares[idCanvas];
    grafico.data.datasets[0].data = [valor, maximo - valor];
    grafico.update();
  } else {
    // Cria novo gráfico
    const novoGrafico = new Chart(canvas, {
      type: 'doughnut',
      data: {
        labels: ['Feito', 'Faltando'],
        datasets: [{
          data: [valor, maximo - valor],
          backgroundColor: ['#4B0082', '#ddd'],
          borderWidth: 0
        }]
      },
      options: {
        cutout: '70%',
        plugins: {
          legend: { display: false },
          tooltip: { enabled: false }
        }
      },
      plugins: ['centerText']
    });

    graficosCirculares[idCanvas] = novoGrafico;
  }
}

// Função para inicializar gráficos circulares dos temas em mobile:
  function inicializarGraficosCirculares() {
    const temas = {
      "Ortografia Geral": "grafico-ortografia-geral",
      "Ortografia": "grafico-ortografia",
      "Uso de Hífen": "grafico-hifen",
      "Acentuação": "grafico-acentuacao",
      "Pronomes": "grafico-pronomes",
      "Figuras de Linguagem": "grafico-figuras",
      "Sintaxe": "grafico-sintaxe",
      "Concordância Verbal": "grafico-concordancia-verbal",
      "Concordância Nominal": "grafico-concordancia-nominal",
      "Regência Verbal": "grafico-regencia",
      "Crase": "grafico-crase",
      "Pontuação": "grafico-pontuacao",
      "Interpretação de Texto": "grafico-interpretacao",
      "Semântica": "grafico-semantica",
      "Coesão e Coerência": "grafico-coesao",
      "Colocação Pronominal": "grafico-colocacao",
      "Redação Oficial": "grafico-redacao",
      "Fonologia": "grafico-fonologia",
      "Morfologia": "grafico-morfologia",
      "Vocabulário": "grafico-vocabulario",
      "Análise Sintática": "grafico-analise-sintatica"
    };

    for (const tema in temas) {
      const canvasId = temas[tema];
      const canvas = document.getElementById(canvasId);
      if (canvas) {
        gerarGraficoCircular(canvasId, 0, 176); // valor inicial 0
      }
    }
  }

// Variável global para guardar o gráfico
let graficoOrtografia;

// Plugin para adicionar texto no centro do gráfico
Chart.register({
  id: 'centerText',
  beforeDraw(chart) {
    const { width } = chart;
    const { height } = chart;
    const ctx = chart.ctx;
    ctx.restore();

    const valor = chart.data.datasets[0].data[0];
    const total = chart.data.datasets[0].data.reduce((a, b) => a + b, 0);
    const porcentagem = Math.round((valor / total) * 100);

    ctx.font = 'bold 14px Arial';
    ctx.textBaseline = 'middle';
    ctx.textAlign = 'center';
    ctx.fillStyle = '#4B0082';
    ctx.fillText(`${porcentagem}%`, width / 2, height / 2);
    ctx.save();
  }
});

// Função para criar ou recriar o gráfico
function criarGraficoOrtografia() {
  const ctx = document.getElementById('grafico-ortografia-graph').getContext('2d');

  // Se já existe, destrói antes de criar outro
  if (graficoOrtografia) {
    graficoOrtografia.destroy();
  }

  graficoOrtografia = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Feijó', 'Relacionar'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19],
        backgroundColor: ['rgba(255, 99, 132)', 'orange']
      }]
    }
  });
}

// Função para deslogar e voltar para tela inicial:
function logout() {
  localStorage.removeItem("ortosmartData");
  window.location.href = "/index.html";
}


// Comando que quando tira a seta de cima ou clica fora do menu, ele fecha */
const sidebar = document.getElementById("sidebar");
const toggle = document.getElementById("toggleSidebar");

// Clique no botão → abre/fecha o menu
toggle.addEventListener("click", (event) => {
  event.stopPropagation(); // impede que o clique se propague pro document
  sidebar.classList.toggle("active");
});

// Clique fora → fecha o menu
document.addEventListener("click", (event) => {
  if (!sidebar.contains(event.target) && event.target !== toggle) {
    sidebar.classList.remove("active");
  }
});



// Função para carregar a primeira questão:
document.addEventListener("DOMContentLoaded", () => {
  carregarQuestao();
  inicializarGraficosCirculares();
  atualizarDica();
  setInterval(atualizarDica, 10000);
});

