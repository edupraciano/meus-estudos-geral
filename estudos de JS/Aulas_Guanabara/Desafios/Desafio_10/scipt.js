function desafio_10() {
  let a = prompt("Qual o valor de a?");
  let b = prompt("Qual o valor de b?");
  let c = prompt("Qual o valor de c?");
  let delta = b ** 2 - 4 * a * c;

  let res = document.getElementById("res");

  res.innerHTML = `A equação atual é: ${a}X <sup>2</sup> + ${b}X + ${c} = 0 <br>
  O cálculo realizado será:  &Delta; = ${b}<sup>2</sup> - 4.${a}.${c} <br>
  O Valor calculado é &Delta; =  ${delta}.`;
}
