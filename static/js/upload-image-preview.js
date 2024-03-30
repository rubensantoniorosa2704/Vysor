// Function to preview the selected image
const previewImage = (event) => {
    const reader = new FileReader();
    reader.onload = () => {
        const output = document.getElementById('image-preview');
        output.src = reader.result;
        output.style.display = 'block';
        sessionStorage.setItem('uploaded-image', reader.result);
    };
    // Read the data URL of the selected file
    reader.readAsDataURL(event.target.files[0]);
}


// When the page is loaded, check if there is an image in the sessionStorage
window.onload = () => {
    const uploadedImage = sessionStorage.getItem('uploaded-image');
    if (uploadedImage) {
        const output = document.getElementById('image-preview');
        output.src = uploadedImage;
        output.style.display = 'block';
    }
}


// Clears sessionStorage when the page is reloaded
window.addEventListener('beforeunload', () => {
    // Clear session storage
    sessionStorage.clear();
});
