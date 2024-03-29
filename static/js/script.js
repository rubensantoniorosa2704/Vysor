document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    uploadImage();
});

function uploadImage() {
    var formData = new FormData();
    var imageFile = document.getElementById('image-upload').files[0];
    formData.append("image", imageFile);

    fetch('/upload-image', {
        method: 'POST',
        body: formData
    }).then(response => {
        console.log('Image uploaded successfully');
    }).catch(error => {
        console.error('Error:', error);
    });
}

function loadImagePreview(event) {
        var imageUpload = document.getElementById('image-upload');
        var imagePreview = document.getElementById('image-preview');

        imagePreview.style.display = 'none'; // Esconde o preview enquanto a imagem não é carregada

        var reader = new FileReader();
        reader.onload = function(e) {
            imagePreview.src = e.target.result;
            imagePreview.style.display = 'block'; // Mostra o preview quando a imagem é carregada
        };

        reader.readAsDataURL(imageUpload.files[0]);
    }