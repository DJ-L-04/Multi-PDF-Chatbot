css = '''
<style>
body {
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
}

.chat-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    height: calc(100vh - 150px);
    overflow-y: auto;
    display: flex;
    flex-direction: column-reverse;
}

.chat-message {
    display: flex;
    align-items: flex-start;  /* Ensures avatar aligns with the top of the message */
    margin-bottom: 15px;
}

.chat-message.bot {
    justify-content: flex-start;
}

.chat-message.user {
    justify-content: flex-end;
}

.message {
    max-width: 60%;
    padding: 10px 15px; /* Smaller padding for a more compact look */
    border-radius: 18px;
    font-size: 14px;  /* Smaller font size for a more compact look */
    line-height: 1.4;
    word-wrap: break-word;
    position: relative;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.chat-message.bot .message {
    background-color: #f1f1f1;
    border-radius: 16px 16px 16px 4px;  /* Rounded top-left for bot */
    color: #333;
}

.chat-message.user .message {
    background-color: #ff4f5e;
    color: white;
    border-radius: 16px 16px 4px 16px;  /* Rounded top-right for user */
    margin-right: 10px;
}

.chat-message .avatar {
    width: 50px;  /* Reduced avatar size */
    height: 50px;
    margin-right: 10px;
}

.chat-message.user .avatar {
    margin-left: 10px;  /* Adjust spacing for user */
    margin-right: 0;
    order: 1;
}

.chat-message .avatar img {
    max-width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}


.input-area {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: white;
    padding: 10px;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    max-width: 800px;
    margin: 0 auto;
    z-index: 10;
}

.input-area input[type="text"] {
    flex-grow: 1;
    padding: 10px 18px;
    border: none;
    border-radius: 30px;
    outline: none;
    font-size: 16px;
    background-color: #f0f0f0;
    margin-right: 10px;
}

.input-area button {
    background-color: #ff4f5e;
    color: white;
    border: none;
    border-radius: 50%;
    width: 45px;
    height: 45px;
    font-size: 20px;
    cursor: pointer;
}

</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">  
    <div class="message">{{MSG}}</div>
    <div class="avatar">
        <img src="cartoon-girl-student-school-happy-icon-vector-11151910.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>  
</div>
'''
