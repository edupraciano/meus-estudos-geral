function desafio_11() {
  let ano = prompt("Qual o Ano que você quer verificar?");
  let res = document.getElementById("res");

  // Converte o ano para um número
  ano = parseInt(ano);

  if ((ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0) {
    res.innerHTML = `O Ano de ${ano} <span style="font-size: 24px; font-weight: bold; background-color:#0ed60e; padding: 0.5rem;"> é Bissexto &#10003; </span> `;
  } else {
    res.innerHTML = `O Ano de ${ano} <span style="font-size: 24px; font-weight: bold; background-color:#e58484; padding: 0.5rem;"> NÃO é Bissexto &#10007; </span> `;
  }
}
