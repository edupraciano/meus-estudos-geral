function contar() {
  let valor_inicio = Number(document.getElementById("inicio").value);
  let valor_fim = Number(document.getElementById("fim").value);
  let valor_passo = Number(document.getElementById("passo").value);
  let resposta = document.getElementById("res");

  if (valor_passo <= 0) {
    alert("Passo inválido, Considerando passo 1");
    valor_passo = 1;
  }
  // Contagem Crescente
  if (valor_inicio < valor_fim) {
    let contagem = "";
    for (let i = valor_inicio; i <= valor_fim; i += valor_passo) {
      contagem += ` ${i} \u{1F449} `;
    }
    resposta.innerHTML = ` ${contagem} \u{1F3C1} `;

    // Contagem Decrescente
  } else {
    let contagem = "";
    for (let i = valor_inicio; i >= valor_fim; i -= valor_passo) {
      contagem += ` ${i} \u{1F449} `;
    }
    resposta.innerHTML = ` ${contagem} \u{1F3C1} `;
  }
}
