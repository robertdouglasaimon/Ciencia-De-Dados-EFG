  const hoje = new Date();
  const diaSemana = hoje.getDay(); // 0 = Domingo, 1 = Segunda, ..., 6 = Sábado

  // Formata a data atual
  const opcoes = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
  const dataFormatada = hoje.toLocaleDateString('pt-BR', opcoes);
  document.getElementById('data-atual').textContent = `Hoje é ${dataFormatada}`;

  // Marca o dia atual e os próximos
  const dias = document.querySelectorAll('.dia-estudo');
  dias.forEach((dia, index) => {
    if (index === diaSemana) {
      dia.classList.add('hoje');
    } else if (index > diaSemana) {
      dia.classList.add('proximo');
    }
  });

