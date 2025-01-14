document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/autenticar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Token recebido:", data.token);
            localStorage.setItem("token", data.token);
            alert("Autenticação bem-sucedida!");
        } else {
            const errorData = await response.json();
            console.error("Erro:", errorData.message);
            alert("Falha na autenticação: " + errorData.message);
        }
    } catch (error) {
        console.error("Erro na requisição:", error);
        alert("Erro na conexão com o servidor.");
    }
});