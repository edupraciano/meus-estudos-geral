function criarLista() {
  let vaiComprar = prompt(
    `Deseja adicionar uma comida na sua lista de compras? Responda com S ou N.`
  );
  let categorias = ["Frutas", "Laticínios", "Congelados", "Doces"];
  let listaDeCompras = {};

  while (vaiComprar.toLowerCase() === "s") {
    let qualComida = prompt("Qual comida você gostaria de comprar?");
    let qualCategoria = mostrarMenuDeCategorias(categorias);

    if (!qualCategoria) {
      alert("Categoria inválida. Escolha uma categoria válida.");
    } else {
      if (!listaDeCompras[qualCategoria]) {
        listaDeCompras[qualCategoria] = [];
      }
      listaDeCompras[qualCategoria].push(qualComida);
    }

    vaiComprar = prompt(
      "Deseja adicionar outra comida na sua lista de compras? Responda com S ou N."
    );
  }

  let listaFinal = "Lista de compras:\n";
  for (const categoria in listaDeCompras) {
    listaFinal += `  ${categoria}: ${listaDeCompras[categoria].join(", ")}\n`;
  }

  alert(listaFinal);
}

function mostrarMenuDeCategorias(categorias) {
  let opcoes = "Escolha a categoria:\n";
  for (let i = 0; i < categorias.length; i++) {
    opcoes += `${i + 1}. ${categorias[i]}\n`;
  }

  let escolha = parseInt(prompt(opcoes)) - 1;

  if (escolha >= 0 && escolha < categorias.length) {
    return categorias[escolha];
  }

  return null;
}

criarLista();
