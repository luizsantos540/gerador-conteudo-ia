const botaoGerar = document.getElementById('btn-gerar');
const textoEntrada = document.getElementById('texto-entrada');
const opcaoProcessamento = document.getElementById('opcao-processamento');
const containerResultado = document.getElementById('resultado-ia');

botaoGerar.addEventListener('click', async () => {
    const texto = textoEntrada.value.trim();
    const opcao = opcaoProcessamento.value;

    if (!texto) {
        alert('Por favor, digite ou cole um texto antes de gerar!');
        return;
    }

    botaoGerar.disabled = true;
    botaoGerar.innerText = 'Processando com IA...';
    containerResultado.innerText = 'Aguarde, analisando o conteúdo...';

    try {
        const resposta = await fetch('http://127.0.0.1:8000/processar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                texto: texto,
                opcao: opcao
            })
        });

        if (!resposta.ok) {
            throw new Error('Erro ao processar a requisição no servidor.');
        }

        const dados = await resposta.json();
        containerResultado.innerText = dados.resultado;

    } catch (erro) {
        containerResultado.innerText = 'Ocorreu um erro ao comunicar com a IA. Verifique se o backend está rodando.';
    } finally {
        botaoGerar.disabled = false;
        botaoGerar.innerText = 'Gerar Conteúdo';
    }
});