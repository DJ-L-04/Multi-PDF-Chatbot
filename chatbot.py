import streamlit as st
from streamlit.components.v1 import html

# Set up the Streamlit page
st.set_page_config(page_title="Chatbot Interface", layout="wide")

st.title("Chatbot Interface")

# CSS for the chat interface, now with avatars above chat bubbles
css = '''
<style>
body {
    background-color: #f0f2f5;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.chat-container {
    flex-grow: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
}

.chat-message {
    padding: 1rem;
    border-radius: 1rem;
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 60%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    word-wrap: break-word;
}

.chat-message.user {
    background-color: #007bff;
    align-self: flex-end;
    color: white;
    border-top-right-radius: 0;
}

.chat-message.bot {
    background-color: #f1f1f1;
    align-self: flex-start;
    border-top-left-radius: 0;
    color: black;
}

.chat-message .avatar {
    width: 50px;
    height: 50px;
    margin-bottom: 0.5rem;  /* Push the avatar above the message */
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    padding: 0.5rem 1rem;
    word-wrap: break-word;
    text-align: center;  /* Center the text in the bubble */
}

.input-container {
    background-color: #fff;
    border-top: 1px solid #e0e0e0;
    padding: 20px;
    position: sticky;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.input-box {
    width: 85%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 20px;
    font-size: 16px;
}

.send-button {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
}

.send-button:hover {
    background-color: #0056b3;
}
</style>
'''

# HTML template for bot messages
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

# HTML template for user messages
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

# JavaScript for sending messages and updating the chat window
javascript = '''
<script>
function botMessage(message) {
    return `
    <div class="avatar">
            <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
        </div>
    <div class="chat-message bot">
        <div class="message">${message}</div>
    </div>
    `;
}

function userMessage(message) {
    return `
    <div class="chat-message user">
        <div class="avatar">
            <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png" alt="User Avatar">
        </div>
        <div class="message">${message}</div>
    </div>
    `;
}

function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (message) {
        const chatContainer = document.getElementById('chat-container');
        chatContainer.innerHTML += userMessage(message);
        input.value = '';
        chatContainer.scrollTop = chatContainer.scrollHeight;
        // Simulate backend response by sending a bot message
        setTimeout(() => {
            chatContainer.innerHTML += botMessage(`You said: ${message}`);
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }, 1000);
    }
}

document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
</script>
'''

# Complete HTML layout
html_code = f'''
{css}

<div class="chat-container" id="chat-container">
    <!-- Chat messages will be appended here -->
</div>

<div class="input-container">
    <input type="text" class="input-box" id="user-input" placeholder="Type your message...">
    <button class="send-button" onclick="sendMessage()">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="22" y1="2" x2="11" y2="13"></line>
            <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
    </button>
</div>

{javascript}
'''

# Embed the complete HTML, CSS, and JavaScript code into the Streamlit app
html(html_code, height=600)
