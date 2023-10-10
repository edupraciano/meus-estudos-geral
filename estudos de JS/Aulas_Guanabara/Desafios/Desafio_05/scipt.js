function desafio_5() {
  let distancia = prompt(`Digite uma distância em metros`);
  let resposta = document.getElementById("res");

  let km = distancia / 1000;
  let Hm = distancia / 100;
  let Dam = distancia / 10;
  let dm = distancia * 10;
  let cm = distancia * 100;
  let mm = distancia * 1000;

  resposta.innerHTML = `A distância de ${distancia} metros, corresponde a... <br> ${km} Kilômetros (Km) <br> ${Hm} Hectrômetros (Hm) <br> ${Dam} Decâmetros (Dam) <br> ${dm} decímetros (dm) <br> ${cm} centímetros (cm) <br> ${mm} milímetros.`;
}
