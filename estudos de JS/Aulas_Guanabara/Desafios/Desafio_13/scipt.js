function desafio_13() {
  let nome = prompt("Qual é o nome do Aluno(a)?");
  let n1 = Number(prompt(`Qual foi a primeira nota de ${nome}`));
  let n2 = Number(prompt(`Qual foi a segunda nota de ${nome}?`));
  let res = document.getElementById("res");

  let n1_format = parseFloat(n1).toFixed(2);
  let n2_format = parseFloat(n2).toFixed(2);

  let media = (n1 + n2) / 2;
  let media_format = media.toFixed(2);
  let situacao = "";

  if (media < 3) {
    situacao = `Com média Abaixo de 3,00 o aluno está <span style="font-size: 18px; font-weight: bold; background-color:#b10606a6; padding: 0.2rem;" > REPROVADO. </span>`;
  } else if (media >= 3 && media < 6) {
    situacao = `Com média acima ou igual a 3,00 e menor do que 6,00 o aluno está de <span style="font-size: 18px; font-weight: bold; background-color:#f5a235a6; padding: 0.2rem;" > RECUPERAÇÃO. </span>`;
  } else {
    situacao = `Com média acima ou igual a 6,00 o aluno está <span style="font-size: 18px; font-weight: bold; background-color:#505beea6; padding: 0.2rem;" > APROVADO. </span>`;
  }

  res.innerHTML = ` <strong> <span style="font-size: 25px;">  Analisando a situação de ${nome},  </span> </strong><br>
  Com as notas ${n1_format} e ${n2_format}, sua média ficou em ${media_format}. <br>
  ${situacao}`;
}
