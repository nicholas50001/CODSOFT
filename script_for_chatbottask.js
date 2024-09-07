document.addEventListener('DOMContentLoaded', () => {
    const sendButton = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const chatboxBody = document.getElementById('chatbox-body');

    sendButton.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            appendMessage('user', userMessage);
            getBotResponse(userMessage);
            userInput.value = '';
        }
    });

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.className = `message ${sender}`;
        messageElement.textContent = message;
        chatboxBody.appendChild(messageElement);
        chatboxBody.scrollTop = chatboxBody.scrollHeight; 
    }

    function getBotResponse(userMessage) {
        let botResponse = '';

        if (userMessage.includes('hello') || userMessage.includes('hi')) {
            botResponse = 'Hello! How can I assist you today?';
        } else if (userMessage.includes('your name')) {
            botResponse = 'I am a simple chatbot created for demonstration purposes.';
        } else if (userMessage.includes('how are you')) {
            botResponse = 'I am only a chatbot program, but I am doing great! How can I help you?';
        } else if (userMessage.includes('bye')) {
            botResponse = 'Goodbye! Have an awesome day!';
        } else if (userMessage.includes('how was your day')) {
            botResponse = 'I am a simple chatbot created for demonstration purposes, but my day went well!';
        } else {
            botResponse = 'I am not sure how to respond to that. Can you ask something else?';
        }

        appendMessage('bot', botResponse);
    }
});
