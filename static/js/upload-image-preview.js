// Função para visualizar a imagem selecionada
const visualizarImagem = (event) => {
    const leitor = new FileReader();
    leitor.onload = () => {
        const output = document.getElementById('image-preview');
        output.src = leitor.result;
        output.style.display = 'block';
        sessionStorage.setItem('uploaded-image', leitor.result);
    };
    // Lê a URL de dados do arquivo selecionado
    leitor.readAsDataURL(event.target.files[0]);
}

// Quando a página é carregada, verifica se há uma imagem no sessionStorage
window.onload = () => {
    const imagemCarregada = sessionStorage.getItem('uploaded-image');
    if (imagemCarregada) {
        const output = document.getElementById('image-preview');
        output.src = imagemCarregada;
        output.style.display = 'block';
    }
}

// Limpa o sessionStorage quando a página é recarregada
window.addEventListener('beforeunload', () => {
    // Limpa o armazenamento de sessão
    sessionStorage.clear();
});
