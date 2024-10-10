// Define uma função assíncrona para lidar com a submissão do formulário
const aoSubmeter = async (event) => {
    event.preventDefault();

    const arquivoImagem = document.querySelector("#file_input").files[0];
    const formData = new FormData();
    formData.append('image', arquivoImagem);

    document.querySelector('#response-section').style.display = 'block';

    const resultado = await fetch("/generate_image", {
        method: 'POST',
        body: formData
    });

    // Retorna o resultado para o HTML, substituindo a primeira letra por maiúscula
    let textoResultado = await resultado.text();
    document.querySelector('#description').innerText = textoResultado.charAt(0).toUpperCase() + textoResultado.slice(1);
};
