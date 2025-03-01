// Função para troca de formulários
function toggleForms() {
    // Seleciona o container principal e alterna a classe "active"
    document.getElementById('content').classList.toggle('active');
}

// Função para chmamar o spineer form cadastro
function spineer_cadastro() {
    // Pegando as variáveis do form
    let name = document.getElementById('name').value.trim()
    let email = document.getElementById('email').value.trim()
    let password = document.getElementById('password').value.trim()

    // Pegando o spineer e o button
    let load = document.getElementById('load_cadastro')
    let btn_cadastro = document.getElementById('btn_cadastro')

    if (name.length < 3) {
        alert('O nome deve ter no mínimmo 3 caracteres!')
        return;
    }

    if (email.length < 12) {
        alert('O email deve ter no mínimo 12 caracteres!')
        return;
    }

    if (password.length < 8) {
        alert('A senha deve ter no mínimo 8 caracteres!')
        return;
    }

    // Caso nenhuma das opções acima aconteça
    btn_cadastro.style.display = "none"
    load.style.display = "flex"

}

// Função para chmamar o spineer form login
function spineer_login() {
    // Pegando as variáveis do form
    let name = document.getElementById('name_login').value.trim()
    let email = document.getElementById('email_login').value.trim()
    let password = document.getElementById('password_login').value.trim()

    // Pegando o spineer e o button
    let load = document.getElementById('load_login')
    let btn_login = document.getElementById('btn_login')

    if (name.length < 3) {
        alert('O nome deve ter no mínimmo 3 caracteres!')
        return;
    }

    if (email.length < 12) {
        alert('O email deve ter no mínimo 12 caracteres!')
        return;
    }

    if (password.length < 8) {
        alert('A senha deve ter no mínimo 8 caracteres!')
        return;
    }

    // Caso nenhuma das opções acima aconteça
    btn_login.style.display = "none"
    load.style.display = "flex"

}