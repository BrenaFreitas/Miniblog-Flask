// Função para aumentar a quantidade
function increase(inputId) {
    const quantityInput = document.getElementById(inputId); // Acessa o input pelo id
    quantityInput.value = parseInt(quantityInput.value) + 1; // Incrementa a quantidade
}

// Função para diminuir a quantidade
function decrease(inputId) {
    const quantityInput = document.getElementById(inputId); // Acessa o input pelo id
    if (quantityInput.value > 1) {
        quantityInput.value = parseInt(quantityInput.value) - 1; // Decrementa a quantidade
    }
}
