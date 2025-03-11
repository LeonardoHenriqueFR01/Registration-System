// Função para alternar a visibilidade da senha em um campo de entrada
function togglePassword(inputId, icon) {
    // Obtém o elemento de input pelo ID fornecido
    const input = document.getElementById(inputId);
    
    // Verifica se o tipo do input é "password"
    if (input.type === "password") {
        // Altera o tipo para "text" para exibir a senha
        input.type = "text";
        icon.innerText = "Visibility";
    } else {
        // Caso contrário, altera o tipo de volta para "password" para ocultar a senha
        input.type = "password";
        icon.innerText = "Visibility_off";
    }
}

// Função para troca de formulários
function toggleForms() {
    // Seleciona o container principal e alterna a classe "active"
    document.getElementById('content').classList.toggle('active');
}

// Função para chamar spin form cadastro
function spin_cadastro() {
    let name = document.getElementById('name').value.trim()
    let email = document.getElementById('email').value.trim()
    let password = document.getElementById('password').value.trim()

    let btn_cadastro = document.getElementById('btn_cadastro')   
    let load_cadastro = document.getElementById('load_cadastro')

    if (name < 3) {
        alert('O nome deve ter no mínimo 3 caracteres!')
        return;
    }

    if (email < 12) {
        alert('O email deve ter no mínimo 12 caracteres!')
        return;
    }

    if (password < 8) {
        alert('A senha deve ter no mínimo 8 caracteres!')
        return;
    }

    // Caso nenhuma das opções a cima ocorra
    btn_cadastro.style.display = "none"
    load_cadastro.style.display = "block"
}

// Função para chamar spin form login
function spin_login() {
    let name = document.getElementById('name_login').value.trim()
    let email = document.getElementById('email_login').value.trim()
    let password = document.getElementById('password_login').value.trim()

    let btn_login = document.getElementById('btn_login')   
    let load_login = document.getElementById('load_login')

    if (name < 3) {
        alert('O nome deve ter no mínimo 3 caracteres!')
        return;
    }

    if (email < 12) {
        alert('O email deve ter no mínimo 12 caracteres!')
        return;
    }

    if (password < 8) {
        alert('A senha deve ter no mínimo 8 caracteres!')
        return;
    }

    // Caso nenhuma das opções a cima ocorra
    btn_login.style.display = "none"
    load_login.style.display = "block"
}
