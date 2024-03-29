// Function to preview the selected image
function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('image-preview');
        output.src = reader.result;
        output.style.display = 'block';
        localStorage.setItem('uploaded-image', reader.result);
    };
    // Read the data URL of the selected file
    reader.readAsDataURL(event.target.files[0]);
}

// When the page is loaded, check if there is an image in the localStorage
window.onload = function() {
    // Retrieve the uploaded image from localStorage
    var uploadedImage = localStorage.getItem('uploaded-image');
    // If an image is found in localStorage
    if (uploadedImage) {
        // Get the image preview element
        var output = document.getElementById('image-preview');
        // Set the source of the image to the one stored in localStorage
        output.src = uploadedImage;
        // Make the image preview visible by changing its display style to 'block'
        output.style.display = 'block';
    }
}
