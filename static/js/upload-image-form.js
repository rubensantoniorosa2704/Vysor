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

    document.querySelector('#description').innerText = await result.text();
}