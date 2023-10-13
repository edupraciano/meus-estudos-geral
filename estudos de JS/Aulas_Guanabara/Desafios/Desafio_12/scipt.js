function desafio_12() {
  let preco_antigo = Number(prompt("Qual era o preço anterior do produto?"));
  let preco_novo = Number(prompt("Qual era o NOVO preço do produto?"));
  let res = document.getElementById("res");
  let diferenca = preco_novo - preco_antigo;
  let diferenca_abs = Math.abs(diferenca);
  let diferenca_abs_format = diferenca_abs.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });
  let preco_antigo_format = preco_antigo.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });
  let preco_novo_format = preco_novo.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  let situação = "";
  let subiu_caiu = "";
  let cima_baixo = "";

  if (preco_antigo > preco_novo) {
    situação = "Mais Barato.";
    subiu_caiu = "caiu";
    cima_baixo = "para baixo";
  } else {
    situação = "Mais Caro.";
    subiu_caiu = "subiu";
    cima_baixo = "para cima";
  }

  let variacao = (preco_novo / preco_antigo - 1) * 100;
  let variacao_format = variacao.toFixed(2);
  let variacao_format_abs = Math.abs(variacao_format);

  res.innerHTML = `Analisando os valores informados, <br>
  O Produto custava ${preco_antigo_format},  e agora custa ${preco_novo_format} . <br>
  Hoje o produto está ${situação}. <br>
  O preco ${subiu_caiu} ${diferenca_abs_format} em relação ao preço anterior. <br>
  Uma variação de ${variacao_format_abs}% ${cima_baixo}.`;
}
