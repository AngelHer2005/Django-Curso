// CSRF:
// Función para obtener el token CSRF desde las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // ¿Empieza esta cadena de cookie con el nombre que queremos?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Obtener el token CSRF
const csrftoken = getCookie('csrftoken');

// AJAX:
fetch('/api/submit/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken // Añadir el token CSRF a las cabeceras
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => {
    console.getElementById("mensaje").innerText = data.message;
})
.catch(error => console.error('Error:', error));
    