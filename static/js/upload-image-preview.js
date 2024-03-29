// Function to preview the selected image
function previewImage(event) {
    let reader = new FileReader();
    reader.onload = function(){
        let output = document.getElementById('image-preview');
        output.src = reader.result;
        output.style.display = 'block';
        sessionStorage.setItem('uploaded-image', reader.result);
    };
    // Read the data URL of the selected file
    reader.readAsDataURL(event.target.files[0]);
}

// When the page is loaded, check if there is an image in the localStorage
window.onload = function() {
    // Retrieve the uploaded image from localStorage
    let uploadedImage = sessionStorage.getItem('uploaded-image');
    // If an image is found in localStorage
    if (uploadedImage) {
        // Get the image preview element
        let output = document.getElementById('image-preview');
        // Set the source of the image to the one stored in localStorage
        output.src = uploadedImage;
        // Make the image preview visible by changing its display style to 'block'
        output.style.display = 'block';
    }
}

// Clears sessionStorage when the page is reloaded
window.addEventListener('beforeunload', function() {
    // Clear session storage
    sessionStorage.clear();
});
