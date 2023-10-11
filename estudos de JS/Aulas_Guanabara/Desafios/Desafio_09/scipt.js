function desafio_9() {
  let nome = prompt("Qual o nome do funcionário?");
  let sal_atual = parseFloat(prompt("Qual é o Salário atual do funcionário?"));
  let sal_atual_formatado = sal_atual.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  let perct_de_aumento = parseFloat(
    prompt("Qual será o percentual de aumento (%) ?")
  );
  let perct_de_aumento_formatado = parseFloat(perct_de_aumento / 100);

  let novo_sal = sal_atual + sal_atual * perct_de_aumento_formatado;
  let novo_sal_formatado = novo_sal.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  let aumento = novo_sal - sal_atual;
  let aumento_formatado = aumento.toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL",
  });

  let res = document.getElementById("res");
  res.innerHTML = ` <strong> <span style="font-size:30px;"  > ${nome} recebeu um aumento salarial! </span> </strong><br>
  O salario atual era de ${sal_atual_formatado}. <br>
  Com o aumento de ${perct_de_aumento}%, O seu Salário irá aumentar ${aumento_formatado} no próximo mês. <br>
  E a partir daí receberá ${novo_sal_formatado}.`;
}
