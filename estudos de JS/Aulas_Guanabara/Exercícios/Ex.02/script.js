function verificar() {
  let data = new Date();
  let ano_atual = data.getFullYear();
  let anoForm = document.getElementById("txt-ano");
  let ano = anoForm.value;
  let res = document.getElementById("resultado");
  var img = document.getElementById("imagem");

  if (ano > ano_atual || ano == "") {
    alert("Preencha o Ano de nascimento corretamente");
  } else {
    let idade = ano_atual - ano;

    let sexoForm = document.getElementsByName("radsex");
    var genero = "";
    let tipo = "";

    if (sexoForm[0].checked) {
      genero = "Um Homem";

      if (idade > 1 && idade <= 15) {
        tipo = "menino";
        res.innerHTML = `Detectamos  ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/menino.jpg";
      } else if (idade > 15 && idade <= 50) {
        tipo = "adulto";
        res.innerHTML = `Detectamos ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/homem.jpg";
      } else if (idade <= 1) {
        tipo = "bebê";
        res.innerHTML = `Detectamos ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/bb_menino.jpg";
      } else if (idade > 50) {
        tipo = "idoso";
        res.innerHTML = `Detectamos ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/velho.jpg";
      }
    } else {
      genero = "Uma Mulher";

      if (idade > 1 && idade <= 15) {
        tipo = "menina";
        res.innerHTML = `Detectamos  ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/menina.jpg";
      } else if (idade > 15 && idade <= 50) {
        tipo = "adulta";
        res.innerHTML = `Detectamos   ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/mulher.jpg";
      } else if (idade <= 1) {
        tipo = "bebê";
        res.innerHTML = `Detectamos   ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/bb_menina.jpg";
      } else if (idade > 50) {
        tipo = "idosa";
        res.innerHTML = `Detectamos  ${genero} ${tipo} com ${idade} anos de idade.`;
        img.src = "./img/velha.jpg";
      }
    }
  }
}
