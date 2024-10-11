// Define an arrow function for the TTS action
const playTextToSpeech = () => {
    const description = document.querySelector('#description').innerText;

    // Create a new instance of SpeechSynthesisUtterance
    const msg = new SpeechSynthesisUtterance(description);

    // Set additional properties (if needed)
    msg.lang = 'pt-BR'; // Set the language (e.g., 'en-US' for United States English)
    msg.rate = 1.0; // Set the speech rate (1.0 is the default)

    // Start speech synthesis
    window.speechSynthesis.speak(msg);
};
