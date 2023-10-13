document.addEventListener('DOMContentLoaded', function () {
    const voiceButton = document.getElementById('voiceButton');

    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        let isRecording = false;
        
        recognition.lang = 'en-US';

        recognition.onresult = event => {
            const transcript = event.results[0][0].transcript;
            console.log('Transcription:', transcript);
            
            // just testing
            alert(transcript);
        };

        recognition.onerror = event => {
            console.error('Speech recognition error:', event.error);
        };

        recognition.onend = () => {
            if (isRecording) {
                recognition.start();
            }
        };

        voiceButton.addEventListener('click', function () {
            if (!isRecording) {
                recognition.start();
                isRecording = true;
                voiceButton.innerText = 'Stop';
            } else {
                recognition.stop();
                isRecording = false;
                voiceButton.innerText = 'Start';
            }
        });
    } else {
        console.error('Speech recognition not supported in this browser');
    }
});