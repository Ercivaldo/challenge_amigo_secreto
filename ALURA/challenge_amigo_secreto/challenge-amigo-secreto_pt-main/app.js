const listaAmigos = [];
const listaElement = document.getElementById("listaAmigos");
const resultadoElement = document.getElementById("resultado");
const inputAmigo = document.getElementById("amigo");

function adicionarAmigo() {
    const nome = inputAmigo.value.trim();

    if (nome === "") {
        alert("Por favor, insira um nome válido.");
        return;
    }

    if (listaAmigos.includes(nome)) {
        alert("Este nome já foi adicionado!");
        return;
    }

    listaAmigos.push(nome);
    atualizarLista();
    inputAmigo.value = "";
    inputAmigo.focus();
}

function atualizarLista() {
    listaElement.innerHTML = "";

    listaAmigos.forEach((amigo, index) => {
        const li = document.createElement("li");
        li.textContent = amigo;
        
        const btnRemover = document.createElement("button");
        btnRemover.textContent = "❌";
        btnRemover.classList.add("remove-button");
        btnRemover.onclick = () => removerAmigo(index);

        li.appendChild(btnRemover);
        listaElement.appendChild(li);
    });
}

function removerAmigo(index) {
    listaAmigos.splice(index, 1);
    atualizarLista();
}

function sortearAmigo() {
    if (listaAmigos.length === 0) {
        alert("Adicione pelo menos um nome antes de sortear.");
        return;
    }

    const sorteado = listaAmigos[Math.floor(Math.random() * listaAmigos.length)];
    resultadoElement.innerHTML = `<li class="sorteado">🎉 ${sorteado} foi sorteado! 🎉</li>`;
}




