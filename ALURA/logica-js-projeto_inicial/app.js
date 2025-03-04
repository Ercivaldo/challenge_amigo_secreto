// Exibe uma mensagem de boas-vindas em um alerta
alert('Boas vindas ao jogo do número secreto');

// Define o número secreto para um número aleatório entre 1 e 100
let numeroMaximo = 30;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1); 

// Imprime o número secreto no console do navegador (útil para debug)
console.log(numeroSecreto);

// Declara a variável 'chute' sem atribuir um valor inicial
let chute;

// Inicializa a variável 'tentativas' com 1
let tentativas = 1;

// Loop continua até que o chute seja igual ao número secreto
while (chute != numeroSecreto) {
    // Solicita ao usuário que escolha um número entre 1 e 100 e converte o valor para um número inteiro
    chute = parseInt(prompt(`Escolha um número entre 1 e ${numeroMaximo}`));

    // Verifica se o chute é um número válido entre 1 e 100
    if (isNaN(chute) || chute < 1 || chute > 100) {
        // Se não for válido, exibe um alerta e volta ao início do loop
        alert('Por favor, insira um número válido entre 1 e 100.');
        continue; // volta ao início do loop
    }

    // Se o chute for igual ao número secreto, exibe uma mensagem de sucesso
    if (chute === numeroSecreto) {
        break;
    } else {
        // Se o chute for maior que o número secreto, informa que o número secreto é menor
        if (chute > numeroSecreto) {
            alert(`O número secreto é menor que o ${chute}`);
        } else {
            // Se o chute for menor que o número secreto, informa que o número secreto é maior
            alert(`O número secreto é maior que o ${chute}`);
        }
        // Incrementa o número de tentativas
        tentativas++;
    }
}

// Corrige a palavra 'tentativas'
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso aí! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);


