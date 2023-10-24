function chutar() {
  let numeroCorreto = Math.floor(
    Math.random() * 9 + 1
  ); /* garante que o numero gerado aleatoriamente esteja ENTRE 0 e 10,
   ou seja, exclui esses números (0 e 10) */
  let tentativas = 3;

  for (let i = 0; i < tentativas; i++) {
    let numeroChutado = parseInt(
      prompt(`Escolha um número entre 1 e 10 para ver como está o seu chute. \n
      Você ainda tem ${tentativas - i} tentativas.`)
    );

    console.log(numeroChutado);

    if (numeroChutado == numeroCorreto) {
      alert(`Parabéns! Você acertou, ${numeroCorreto} era o número inicial.`);
      return; // Encerra a função se acertar
    } else {
      alert(
        `Você não acertou, mas não se preocupe, você ainda tem ${
          tentativas - i - 1
        } tentativas restantes. Tente novamente.`
      );
    }
  }

  alert(
    `Infelizmente você não acertou nenhuma das tentativas. O número correto era ${numeroCorreto}. \n
    Tente novamente.`
  );
}
