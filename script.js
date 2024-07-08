// Captura o formulário e a caixa de entrada de mensagem
var form = document.getElementById('user-form');
var userInput = document.getElementById('user-input');

// Adiciona um evento de envio para o formulário
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Obtém o valor da caixa de entrada de mensagem
    var messageText = userInput.value.trim();

    if (messageText !== '') {
        // Adiciona a mensagem do usuário ao chat
        adicionarMensagem('Você', messageText, 'user-message');

        // Limpa a caixa de entrada de mensagem
        userInput.value = '';

        // Simula a resposta do bot (exemplo simples)
        var botResponse = "Olá! Seja bem-vindo ao chat de vendas da Delta Ti, vou te direcionar para nossa vendedora virtual";
        adicionarMensagem('Eliz', botResponse, 'bot-message');

        // Scroll automático para o final do chat
        scrollChat();
    }
});

// Função para adicionar mensagem ao chat
function adicionarMensagem(nome, texto, classe) {
    var chatOutput = document.getElementById('chat-output');

    var messageElement = document.createElement('div');
    messageElement.className = 'message ' + classe;
    messageElement.innerHTML = `<p>${nome}: ${texto}</p>`;
    chatOutput.appendChild(messageElement);
}

// Função para scroll automático do chat
function scrollChat() {
    var chatOutput = document.getElementById('chat-output');
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

// Atualiza o ano no rodapé
document.getElementById('ano-atual').textContent = new Date().getFullYear();
