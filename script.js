// Aguarda o conteúdo da página carregar completamente
document.addEventListener('DOMContentLoaded', () => {

    // Seleciona os elementos do HTML
    const pesoInput = document.getElementById('peso');
    const alturaInput = document.getElementById('altura');
    const calcularBtn = document.getElementById('calcularBtn');
    const resultadoDiv = document.getElementById('resultado');

    // Adiciona um "ouvinte" de evento ao botão
    calcularBtn.addEventListener('click', () => {
        // Pega os valores dos campos e converte para número
        const peso = parseFloat(pesoInput.value);
        const altura = parseFloat(alturaInput.value);

        // Limpa classes de estilo anteriores do resultado
        resultadoDiv.classList.remove('success', 'error');
        resultadoDiv.innerHTML = ''; // Limpa o conteúdo anterior

        // Validação dos dados de entrada
        if (isNaN(peso) || isNaN(altura) || peso <= 0 || altura <= 0) {
            resultadoDiv.textContent = 'Por favor, insira valores válidos.';
            resultadoDiv.classList.add('error');
            return; // Interrompe a função aqui
        }

        // Calcula o IMC
        const imc = peso / (altura * altura);

        // Obtém a classificação baseada no valor do IMC
        const classificacao = getClassificacaoIMC(imc);

        // Exibe o resultado formatado
        resultadoDiv.innerHTML = `Seu IMC é <strong>${imc.toFixed(2)}</strong><br>Classificação: <strong>${classificacao}</strong>`;
        resultadoDiv.classList.add('success');
    });

    // Função para determinar a classificação do IMC
    function getClassificacaoIMC(imc) {
        if (imc < 18.5) {
            return "Abaixo do peso";
        } else if (imc <= 24.9) {
            return "Peso normal";
        } else if (imc <= 29.9) {
            return "Sobrepeso";
        } else if (imc <= 34.9) {
            return "Obesidade Grau I";
        } else if (imc <= 39.9) {
            return "Obesidade Grau II";
        } else {
            return "Obesidade Grau III";
        }
    }
});