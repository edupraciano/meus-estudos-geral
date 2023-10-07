function carregar() {
  let msg = window.document.getElementById("msg");
  let img = window.document.getElementById("imagem");
  let data = new Date();
  let hora = data.getHours();
  hora = 4;

  if (hora < 12 && hora >= 6) {
    let tipo = "Manhã.";
    msg.innerHTML = ` Bom Dia, <br> Agora são ${hora} horas da ${tipo}`;
    img.src = "./img/manha.jpg";
    document.body.style.background = "#faf3cbfb";
  } else if (hora >= 12 && hora < 18) {
    let tipo = "Tarde.";
    msg.innerHTML = ` Boa tarde, <br> Agora são ${hora}  horas da ${tipo}`;
    img.src = "./img/tarde.jpg";
    document.body.style.background = "#eed35bb2";
  } else if (hora >= 18 && hora < 24) {
    let tipo = "Noite.";
    msg.innerHTML = ` Boa noite, <br> Agora são ${hora}  horas da ${tipo}`;
    img.src = "./img/noite.jpg";
    document.body.style.background = "#0e0e0efb";
  } else {
    let tipo = "Madrugada.";
    msg.innerHTML = ` Boa Madrugada, <br> Agora são ${hora} horas da ${tipo}`;
    img.src = "./img/noite.jpg";
    document.body.style.background = "#0e0e0efb";
  }
}
