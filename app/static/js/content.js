// Função para chamar button spin
function get_spin() {
    let name = document.getElementById('name').value.trim()
    let age = document.getElementById('age').value.trim()

    let btn_client_cadastro = document.getElementById('btn_client_cadastro')
    let load = document.getElementById('load')

    if (name < 3) {
        alert('O nome deve ter no mínimo 3 caracteres!')
        return;
    }

    if (age < 1) {
        alert('A idade não pode ficar vazia!')
        return;
    }

    // Caso nenhuma das opções a cima ocorra
    btn_client_cadastro.style.display = "none"
    load.style.display = "block"

}