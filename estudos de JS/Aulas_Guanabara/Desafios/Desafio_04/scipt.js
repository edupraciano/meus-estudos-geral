let produto = prompt(`Qual produto você está comprando?`);
let preco = prompt(`Quanto custa o ${produto} que você está comprando?`);
let dinheiro = prompt(
  `Quanto você tem em dinheiro para comprar o ${produto} que você comprou?`
);
let troco = dinheiro - preco;

function desafio_4() {
  if (preco > dinheiro) {
    alert(
      `${produto} custa mais caro do que você tem no momento. \n Retorne com o valor correto para comprar este produto.`
    );
  } else {
    if (
      preco == 0 ||
      preco == "" ||
      dinheiro == 0 ||
      dinheiro == "" ||
      preco < 0 ||
      dinheiro < 0
    ) {
      alert("Dados incorretos ou faltando. Verifique novamente.");
    } else {
      alert(
        `Você comprou um ${produto} que custou ${preco}. \n Deu ${dinheiro} em dinheiro e vai receber ${troco} de troco. \n Volte Sempre.`
      );
    }
  }
}
