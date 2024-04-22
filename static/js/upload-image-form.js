// Define an asynchronous function to handle form submission
const onSubmit = async (event) => {
    event.preventDefault();

    const fileImage = document.querySelector("#file_input").files[0];
    const formData = new FormData();
    formData.append('image', fileImage);

    document.querySelector('#response-section').style.display = 'block';

    const result = await fetch("/generate_image", {
        method:'POST',
        body:formData
    });

    // Returns the result to html, replacing the first letter with uppercase
    let resultText = await result.text();
    document.querySelector('#description').innerText = resultText.charAt(0).toUpperCase() + resultText.slice(1);
}