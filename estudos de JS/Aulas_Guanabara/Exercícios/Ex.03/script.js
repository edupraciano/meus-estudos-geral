function calcular() {
  let num = document.getElementById("txtn");
  let resposta = document.getElementById("res");
  let n = num.value;

  if (n == "") {
    alert(
      "Escolha um número DIFERENTE de ZERO para que possa te mostrar a tabuada."
    );
  } else {
    let tabuada = "";
    for (let i = 1; i <= 10; i++) {
      tabuada += `${n} X ${i} = ${n * i} <br>`;
    }
    resposta.innerHTML = tabuada;
  }
}
