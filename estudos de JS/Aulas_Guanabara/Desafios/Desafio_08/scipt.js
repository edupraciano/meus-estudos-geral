function desafio_8() {
  let produto = prompt("Qual o produto  que você está comprando?");
  let preco_original = Number(
    prompt(`Qual o preço de ${produto} que você está comprando?`)
  );
  let res = document.getElementById("res");

  let selectDesconto = document.getElementById("percentualDesconto");
  let valor_do_desconto = parseFloat(selectDesconto.value);

  let preco_com_desconto = preco_original - preco_original * valor_do_desconto;

  let diferenca = preco_original - preco_com_desconto;

  let preco_original_formatado = preco_original.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  let preco_com_desconto_formatado = preco_com_desconto.toLocaleString(
    "pt-BR",
    {
      style: "currency",
      currency: "BRL",
    }
  );

  let diferenca_formatado = diferenca.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  res.innerHTML = ` <strong> <span style="font-size: 30px;"> Calculando desconto de ${
    valor_do_desconto * 100
  }% para ${produto}.</span> </strong> <br>
  O preço original era ${preco_original_formatado}. <br>
  Você acaba de ganhar um desconto de ${diferenca_formatado} ( - ${
    valor_do_desconto * 100
  }%). <br>
  No fim, você irá pagar ${preco_com_desconto_formatado} no produto ${produto}.`;
}
