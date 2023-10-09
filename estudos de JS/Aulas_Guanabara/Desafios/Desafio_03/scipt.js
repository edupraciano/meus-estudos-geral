function desafio_3() {
  let numero = Number(prompt("Digite um Número qualquer."));

  let antecessor = numero - 1;
  let sucessor = numero + 1;

  alert(
    `O numero digitado foi ${numero} \n O seu antecessor é ${antecessor}. \n E o seu sucessor ${sucessor}`
  );
}
