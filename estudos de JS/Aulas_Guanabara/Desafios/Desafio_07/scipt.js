var cotacao = 0;

function carregarAoIniciar() {
  cotacao = Number(prompt("Qual é a cotaçao do Dolár?"));
}

function desafio_7() {
  let dinheiro = Number(prompt("Quantos Reais você quer converter?"));

  let dinheiroConvertido = dinheiro.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  let dolar = dinheiro * cotacao;
  let res = document.getElementById("res");

  res.innerHTML = `Com ${dinheiroConvertido} pela cotação de ${cotacao},
  você conseguirá comprar UU$ ${dolar.toFixed(2)}.`;
}
