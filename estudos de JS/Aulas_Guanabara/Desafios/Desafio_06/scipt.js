function desafio_6() {
  let tempC = Number(prompt(`Digite uma temperatura em graus Celcius ºC`));
  let tempF = tempC * 1.8 + 32;
  let tempK = tempC + 273.15;

  let resposta = document.getElementById("res");

  resposta.innerHTML = `A temperatura de ${tempC} graus Celcius corresponde a: \n ${tempF} graus Fahrenheit e \n ${tempK} graus Kelvin.`;
}
