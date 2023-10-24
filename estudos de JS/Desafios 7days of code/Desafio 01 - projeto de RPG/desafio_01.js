//document.addEventListener("DOMContentLoaded", main);

var escolha = ""; // Variável para armazenar a escolha do usuário

function verificar() {
  let inputFrontEnd = document.querySelector("#frontEnd");
  let inputBackEnd = document.querySelector("#backEnd");

  if (inputFrontEnd.checked) {
    escolha = "Front-End";
    console.log(`Opção ${escolha} foi escolhida`);
  } else if (inputBackEnd.checked) {
    escolha = "Back-End";
    console.log(`Opção ${escolha} foi escolhida`);
  }
}

function rodar() {
  var opcao = "";

  if (escolha === "Front-End") {
    opcao = prompt(`Ótima Escolha! \n
    Já que você escolheu se especializar em ${escolha},  \n 
    qual opção você gostaria de aprender: 'REACT' ou 'VUE'? \n
    Caso Prefira 'REACT' digite: 1, caso prefira 'VUE', digite: 2 `);
  } else if (escolha === "Back-End") {
    opcao = prompt(`Ótima Escolha! \n
    Já que você escolheu se especializar em ${escolha},  \n
    qual dessas linguagens de programação você gostaria de aprender: 'JAVA' ou '#C'? \n
    Caso Prefira 'JAVA' digite: 3, caso prefira '#C', digite: 4 `);
  }

  var segundaOpcao = "";
  if (opcao === "1") {
    segundaOpcao = "REACT";
    console.log("Você escolheu REACT.");
  } else if (opcao === "2") {
    segundaOpcao = "VUE";
    console.log("Você escolheu VUE.");
  } else if (opcao === "3") {
    segundaOpcao = "#C";
    console.log("Você escolheu #C.");
  } else if (opcao === "4") {
    segundaOpcao = "JAVA";
    console.log("Você escolheu JAVA.");
  }

  var tecnologias = [];
  var continuar = true;

  while (continuar) {
    var tecnologiaEscolhida = prompt(
      "Quais são as tecnologias nas quais você gostaria de se especializar ou de conhecer?"
    );
    tecnologias.push(tecnologiaEscolhida);

    var repetirAPergunta = prompt(
      "Ainda gostaria de aprender mais alguma tecnologia? (Responda 'sim' ou 'não')"
    );

    if (repetirAPergunta.toLowerCase() === "não") {
      continuar = false;
    }
  }

  let saida = document.querySelector("#res");
  saida.textContent = `As suas escolhas foram: ${tecnologias.join(", ")}`;
}
