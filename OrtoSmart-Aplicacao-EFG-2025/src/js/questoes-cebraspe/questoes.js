const questoes = [
  {
    tema: "Ortografia",
    enunciado: "Assinale a alternativa que apresenta a grafia correta:",
    alternativas: ["Exceção", "Excessão", "Eceção", "Ecessão"],
    correta: 0,
    comentario: "A forma correta é 'Exceção', com X e Ç.",
    banca: "CESPE/CEBRASPE",
    ano: 2021
  },
  {
    tema: "Acentuação",
    enunciado: "Qual das palavras abaixo está corretamente acentuada?",
    alternativas: ["Juri", "Trafego (substantivo: trânsito)", "Anéis", "Heroi"],
    correta: 2,
    comentario: "'Anéis' está correta, conforme a regra das oxítonas terminadas em 'eis'.",
    banca: "ENEM",
    ano: 2019
  },
  {
    tema: "Concordância Verbal",
    enunciado: "Assinale a frase correta quanto à concordância verbal:",
    alternativas: [
      "Fazem dois anos que ele saiu.",
      "Faz dois anos que ele saiu.",
      "Fazem muitos barulhos nesta sala.",
      "Fazem-se dois anos que ele saiu."
    ],
    correta: 1,
    comentario: "O verbo 'fazer', indicando tempo decorrido, é impessoal e deve ficar no singular.",
    banca: "CESPE/CEBRASPE",
    ano: 2020
  },
  {
    tema: "Concordância Nominal",
    enunciado: "Assinale a alternativa correta quanto à concordância nominal:",
    alternativas: [
      "Estava meio preocupada com a prova.",
      "Estava meia preocupada com a prova.",
      "Ela ficou meio chateada e meia triste.",
      "Elas estavam meio cansados."
    ],
    correta: 0,
    comentario: "A palavra 'meio', no sentido de 'um pouco', é invariável.",
    banca: "CESPE/CEBRASPE",
    ano: 2018
  },
  {
    tema: "Regência Verbal",
    enunciado: "Assinale a frase correta quanto à regência verbal:",
    alternativas: [
      "Assisti o filme ontem.",
      "Assisti ao filme ontem.",
      "Assisti aquele filme ontem.",
      "Assisti esse filme ontem sem a preposição."
    ],
    correta: 1,
    comentario: "O verbo 'assistir' no sentido de ver exige a preposição 'a'.",
    banca: "CESPE/CEBRASPE",
    ano: 2019
  },
  {
    tema: "Crase",
    enunciado: "Assinale a alternativa em que o uso da crase está correto:",
    alternativas: [
      "Vou à escola todos os dias.",
      "Cheguei à pé no trabalho.",
      "Assisti à uma peça de teatro.",
      "Entreguei o relatório à ele."
    ],
    correta: 0,
    comentario: "O uso da crase em 'à escola' está correto, pois é verbo + preposição + artigo definido feminino.",
    banca: "CESPE/CEBRASPE",
    ano: 2021
  },
  {
    tema: "Pontuação",
    enunciado: "Assinale a alternativa cuja pontuação está correta:",
    alternativas: [
      "Maria, João e Pedro foram ao mercado.",
      "Maria João, e Pedro foram ao mercado.",
      "Maria João e, Pedro foram ao mercado.",
      "Maria João e Pedro, foram ao mercado."
    ],
    correta: 0,
    comentario: "A vírgula separa elementos de uma enumeração, exceto antes da conjunção 'e'.",
    banca: "ENEM",
    ano: 2017
  },
  {
    tema: "Pronomes",
    enunciado: "Assinale a alternativa em que o uso do pronome está correto:",
    alternativas: [
      "Entre eu e você não há segredos.",
      "Entre mim e você não há segredos.",
      "Entre eu e tu não há segredos.",
      "Entre eu e ele não há segredos."
    ],
    correta: 1,
    comentario: "Após preposição, deve-se usar a forma oblíqua: 'mim'.",
    banca: "CESPE/CEBRASPE",
    ano: 2020
  },
  {
    tema: "Figuras de Linguagem",
    enunciado: "Na frase 'O vento beijava o rosto da menina', há ocorrência de:",
    alternativas: ["Metáfora", "Prosopopeia", "Hipérbole", "Metonímia"],
    correta: 1,
    comentario: "Prosopopeia: atribuição de características humanas a seres inanimados.",
    banca: "ENEM",
    ano: 2018
  },
  {
    tema: "Sintaxe",
    enunciado: "Assinale a alternativa em que o sujeito é indeterminado:",
    alternativas: [
      "Vive-se bem naquela cidade.",
      "Choveu bastante ontem.",
      "As crianças brincavam no parque.",
      "O livro foi lido por João."
    ],
    correta: 0,
    comentario: "Em 'Vive-se bem...', o sujeito é indeterminado pelo uso da partícula 'se'.",
    banca: "CESPE/CEBRASPE",
    ano: 2019
  },
  {
    tema: "Semântica",
    enunciado: "Assinale a alternativa em que há ambiguidade de sentido:",
    alternativas: [
      "O policial viu o homem com binóculos.",
      "Os alunos estudaram bastante.",
      "A professora corrigiu as provas ontem.",
      "O cachorro latiu a noite inteira."
    ],
    correta: 0,
    comentario: "Pode-se entender que o policial usou binóculos ou que o homem estava com binóculos.",
    banca: "CESPE/CEBRASPE",
    ano: 2017
  },
  {
    tema: "Interpretação de Texto",
    enunciado: "Segundo as orientações do Cebraspe, a interpretação correta de um texto deve:",
    alternativas: [
      "Basear-se apenas em opinião pessoal.",
      "Restringir-se às informações apresentadas.",
      "Considerar apenas conhecimentos prévios do candidato.",
      "Ser sempre subjetiva."
    ],
    correta: 1,
    comentario: "A interpretação deve ser fiel ao texto, sem extrapolações indevidas.",
    banca: "CESPE/CEBRASPE",
    ano: 2018
  },
  {
    tema: "Coesão e Coerência",
    enunciado: "Na frase 'Ele não estudou, portanto foi mal na prova', o conectivo 'portanto' expressa:",
    alternativas: ["Causa", "Consequência", "Adversidade", "Condição"],
    correta: 1,
    comentario: "O conectivo 'portanto' estabelece relação de consequência.",
    banca: "ENEM",
    ano: 2020
  },
  {
    tema: "Colocação Pronominal",
    enunciado: "Assinale a alternativa que respeita a norma culta quanto à colocação pronominal:",
    alternativas: [
      "Me disseram que você viria.",
      "Disseram-me que você viria.",
      "Eles me disseram que viria você.",
      "Lhe disseram que você viria."
    ],
    correta: 1,
    comentario: "O uso de 'disseram-me' está adequado, pois o verbo inicia a oração e atrai o pronome.",
    banca: "CESPE/CEBRASPE",
    ano: 2022
  },
  {
    tema: "Redação Oficial",
    enunciado: "Na redação oficial, é incorreto:",
    alternativas: [
      "Usar linguagem clara e objetiva.",
      "Empregar pronomes de tratamento corretamente.",
      "Utilizar linguagem coloquial e subjetiva.",
      "Manter impessoalidade no texto."
    ],
    correta: 2,
    comentario: "Na redação oficial, a linguagem deve ser formal, impessoal e clara.",
    banca: "CESPE/CEBRASPE",
    ano: 2016
  },
  {
    tema: "Fonologia",
    enunciado: "Em qual alternativa todas as palavras possuem ditongo?",
    alternativas: [
      "Caixa, peixe, coisa",
      "Pato, mesa, rio",
      "Copo, casa, flor",
      "Verde, bola, homem"
    ],
    correta: 0,
    comentario: "'Caixa', 'peixe' e 'coisa' possuem ditongos.",
    banca: "ENEM",
    ano: 2015
  },
  {
    tema: "Morfologia",
    enunciado: "Assinale a alternativa em que a palavra destacada é um advérbio:",
    alternativas: [
      "Ele chegou cedo.",
      "O livro é interessante.",
      "A casa é bonita.",
      "Ele é médico."
    ],
    correta: 0,
    comentario: "Advérbio é a palavra que modifica o verbo, como em 'chegou cedo'.",
    banca: "CESPE/CEBRASPE",
    ano: 2017
  },
  {
    tema: "Vocabulário",
    enunciado: "O antônimo de 'efêmero' é:",
    alternativas: ["Duradouro", "Passageiro", "Curto", "Breve"],
    correta: 0,
    comentario: "'Efêmero' significa de curta duração; seu antônimo é 'duradouro'.",
    banca: "ENEM",
    ano: 2016
  },
  {
    tema: "Análise Sintática",
    enunciado: "Na frase 'Os alunos estudam bastante', o termo 'bastante' exerce a função de:",
    alternativas: [
      "Objeto direto",
      "Adjunto adverbial de intensidade",
      "Predicativo do sujeito",
      "Complemento nominal"
    ],
    correta: 1,
    comentario: "'Bastante' indica intensidade do verbo, sendo adjunto adverbial de intensidade.",
    banca: "CESPE/CEBRASPE",
    ano: 2018
  }
  
];
