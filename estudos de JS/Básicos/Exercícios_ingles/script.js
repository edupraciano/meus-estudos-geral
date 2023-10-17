function ex_01() {
  // Define informações da função ex_01
  let lutador = "Fedor Emelianenko";
  let nacionalidade = "Russo";
  let idade = 44;
  let peso = 106;
  let altura = 1.83;

  // Atualiza o conteúdo da seção 1 e mantém o título da seção
  let res1 = document.getElementById("p1");
  res1.innerHTML = ` Lutador: ${lutador} <br>
                    Nacionalidade: ${nacionalidade} <br>
                    Idade: ${idade} anos <br>
                    Peso: ${peso} Kg <br>
                    Altura: ${altura} m `;

  // Apaga o conteúdo das outras seções
  let res2 = document.getElementById("p2");
  res2.innerHTML = "";
  let res3 = document.getElementById("p3");
  res3.innerHTML = "";
  let res4 = document.getElementById("p4");
  res4.innerHTML = "";
}

function ex_02() {
  // Define informações da função ex_02
  const dia = 10;
  const mes = 9;
  const ano = 2021;
  const data = dia + "/" + mes + "/" + ano;
  const frase = "Frase de Efeito para teste";
  const autor = "'Eduardo Praciano'";

  // Atualiza o conteúdo da seção 2 e mantém o título da seção
  let res2 = document.getElementById("p2");
  res2.innerHTML = ` ${data} <br>
                    ${frase} <br>
                    ${autor}`;

  // Apaga o conteúdo das outras seções
  let res1 = document.getElementById("p1");
  res1.innerHTML = "";
  let res3 = document.getElementById("p3");
  res3.innerHTML = "";
  let res4 = document.getElementById("p4");
  res4.innerHTML = "";
}

function ex_03() {
  let meses = [
    "Janeiro,",
    "Fevereiro,",
    "Março,",
    "Abril,",
    "Maio,",
    "Junho,",
    "Julho,",
    "Agosto,",
    "Setembro,",
    "Outubro,",
    "Novembro,",
    "Dezembro",
  ];

  let res3 = document.getElementById("p3");

  res3.innerHTML = meses.join(" ");
  // Apaga o conteúdo das outras seções
  let res1 = document.getElementById("p1");
  res1.innerHTML = "";
  let res2 = document.getElementById("p2");
  res2.innerHTML = "";
  let res4 = document.getElementById("p4");
  res4.innerHTML = "";
}

function ex_04() {
  let obj = {
    nome: "Hearthstone",
    desenvolvedor: "Blizzard",
    ano: 2012,
  };

  let res4 = document.getElementById("p4");

  res4.innerHTML = `Jogo: ${obj.nome} <br>
                   Desenvolvedor: ${obj.desenvolvedor} <br>
                   Ano de Lançamento: ${obj.ano}`;

  // Apaga o conteúdo das outras seções
  let res1 = document.getElementById("p1");
  res1.innerHTML = "";
  let res2 = document.getElementById("p2");
  res2.innerHTML = "";
  let res3 = document.getElementById("p3");
  res3.innerHTML = "";
}
