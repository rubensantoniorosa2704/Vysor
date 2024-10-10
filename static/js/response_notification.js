// Define uma função de seta para a ação de TTS (Texto para Fala)
const reproduzirTextoParaFala = () => {
    const descricao = document.querySelector('#description').innerText;

    // Cria uma nova instância de SpeechSynthesisUtterance
    const msg = new SpeechSynthesisUtterance(descricao);

    // Define propriedades adicionais (se necessário)
    msg.lang = 'pt-BR'; // Define o idioma (por exemplo, 'en-US' para inglês dos Estados Unidos)
    msg.rate = 1.0; // Define a taxa de fala (1.0 é o padrão)

    // Inicia a síntese de fala
    window.speechSynthesis.speak(msg);
};
