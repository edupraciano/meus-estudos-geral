const array = [1, 2, 3];

function sumArray(array) {
  let soma = 0;

  for (let i = 0; i < array.length; i++) {
    soma += array[i];
  }
  return soma;
}

const result = sumArray(array);

console.log(result);
