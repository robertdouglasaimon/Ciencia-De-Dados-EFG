function analisarRedacao() {
  const titulo = document.getElementById("titulo-redacao").value.trim();
  const texto = document.getElementById("texto-redacao").value.trim();
  const resultadoDiv = document.getElementById("resultado-redacao");

  if (!texto) {
    resultadoDiv.innerHTML = "<p style='color: red;'>Por favor, escreva sua redação antes de analisar.</p>";
    return;
  }
    // Obtenha a data atual
  const dataAtual = new Date();
  const dataFormatada = dataAtual.toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "long",
    year: "numeric" 
  });


  // 🔍 Pré-processamento
  const textoLimpo = texto.toLowerCase();
  const paragrafos = texto.split(/\n+/).filter(p => p.trim().length > 0).length;
  const palavras = texto.split(/\s+/).filter(p => p.trim().length > 0);
  const tamanho = palavras.length;

  // ✅ Critérios
  const conectivos = ["portanto", "além disso", "logo", "porém", "todavia", "entretanto", "assim", "dessa forma"];
  const conectivosUsados = conectivos.filter(c => textoLimpo.includes(c));
  const sinaisPontuacao = texto.match(/[.,;:!?]/g) || [];
  const errosOrtograficos = texto.match(/\b[a-z]{3,}[^a-z\s]/gi) || [];

  const temIntroducao = textoLimpo.includes("neste texto") || textoLimpo.includes("iremos abordar") || textoLimpo.includes("a presente redação");
  const temConclusao = textoLimpo.includes("em conclusão") || textoLimpo.includes("portanto") || textoLimpo.includes("dessa forma");

  const vocabularioTecnico = ["segurança pública", "direitos fundamentais", "normas legais", "constituição", "jurisdição", "repressão", "investigação", "crime", "lei"];
  const termosTecnicosUsados = vocabularioTecnico.filter(t => textoLimpo.includes(t));

  const verbos = texto.match(/\b[a-z]{2,}ar\b|\b[a-z]{2,}er\b|\b[a-z]{2,}ir\b/gi) || [];
  const vozAtiva = textoLimpo.includes("o autor afirma") || textoLimpo.includes("o cidadão exige") || textoLimpo.includes("a polícia atua");

  // 🧮 Avaliação
  const notaEstrutura = temIntroducao && temConclusao ? 20 : 15;
  const notaParagrafos = paragrafos >= 3 ? 20 : 12;
  const notaConectivos = conectivosUsados.length >= 2 ? 20 : 14;
  const notaPontuacao = sinaisPontuacao.length >= 10 ? 20 : 13;
  const notaOrtografia = errosOrtograficos.length <= 3 ? 20 : 10;
  const notaCoesao = conectivosUsados.length >= 3 && temConclusao ? 20 : 14;
  const notaVocabulario = termosTecnicosUsados.length >= 3 ? 20 : 12;
  const notaTamanho = tamanho >= 200 ? 20 : 10;
  const notaVerbal = vozAtiva ? 20 : 14;
  const notaTitulo = titulo.length > 5 ? 20 : 10;

  const notaFinal = Math.round(
    (notaEstrutura + notaParagrafos + notaConectivos + notaPontuacao + notaOrtografia +
     notaCoesao + notaVocabulario + notaTamanho + notaVerbal + notaTitulo) / 10
  );

  // 🧾 Resultado
resultadoDiv.innerHTML = `
  <h3>${titulo || "Redação sem título"} <span style="font-weight: normal; font-size: 0.9em; color: #666;">— ${dataFormatada}</span></h3>


  <h4 style="margin-top: 1em;">Análise Técnica</h4>
  <ul style="list-style-type: none; padding-left: 0;">
    <li><strong>Parágrafos:</strong> ${paragrafos}</li>
    <li><strong>Palavras:</strong> ${tamanho}</li>
    <li><strong>Conectivos usados:</strong> ${conectivosUsados.join(", ") || "Nenhum detectado"}</li>
    <li><strong>Termos técnicos:</strong> ${termosTecnicosUsados.join(", ") || "Nenhum detectado"}</li>
    <li><strong>Erros ortográficos (estimado):</strong> ${errosOrtograficos.length}</li>
    <li><strong>Sinais de pontuação:</strong> ${sinaisPontuacao.length}</li>
    <li><strong>Voz ativa detectada:</strong> ${vozAtiva ? "Sim" : "Não"}</li>
  </ul>

  <h4 style="margin-top: 1em;">Notas por Critério</h4>
  <ul style="list-style-type: none; padding-left: 0;">
    <li><strong>Ortografia:</strong> ${notaOrtografia}/20 — uso correto de acentuação e caracteres especiais</li>
    <li><strong>Argumentação:</strong> ${notaVocabulario}/20 — profundidade e extensão do texto</li>
    <li><strong>Coesão:</strong> ${notaCoesao}/20 — uso de conectivos como "portanto", "além disso"</li>
    <li><strong>Estrutura:</strong> ${notaEstrutura}/20 — presença de parágrafos e organização</li>
    <li><strong>Parágrafos:</strong> ${notaParagrafos}/20</li>
    <li><strong>Conectivos:</strong> ${notaConectivos}/20</li>
    <li><strong>Pontuação:</strong> ${notaPontuacao}/20</li>
    <li><strong>Tamanho:</strong> ${notaTamanho}/20</li>
    <li><strong>Voz ativa:</strong> ${notaVerbal}/20</li>
    <li><strong>Título:</strong> ${notaTitulo}/20</li>
  </ul>

  <h3 style="margin-top: 1em;">Nota Final: ${notaFinal}/20</h3>
  <p><em>Avaliação simulada com base em critérios técnicos de concursos federais estilo Cebraspe.</em></p>
`;

  // Limpa inputs da redação:
  document.getElementById("titulo-redacao").value = "";
  document.getElementById("texto-redacao").value = "";
  document.getElementById("upload-redacao").value = "";
}

