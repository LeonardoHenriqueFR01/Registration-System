// Pegando os conteúdos
let cont_cadastrar = document.getElementById('cadastrar')
let cont_cadastrados = document.getElementById('cadastrados')


// Função para chamar área de cadastrados
function cadastrados_get() {
    cont_cadastrar.style.display = "none"
    cont_cadastrados.style.display = "block"
}

// Função para chamar área de cadastrar
function cadastrar_get() {
    cont_cadastrados.style.display = "none"
    cont_cadastrar.style.display = "flex"
}

