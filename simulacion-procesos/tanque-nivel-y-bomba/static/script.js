document.addEventListener("DOMContentLoaded", () => {
    const bombaEncendida = document.body.dataset.bomba === "true";
    const tiempoInicial = parseInt(document.body.dataset.tiempo, 10) || 0;

    const tiempoBombaEl = document.getElementById("tiempoBomba");
    const liquido = document.getElementById("liquid");
    const tank = document.querySelector(".tank");

    let tiempo = tiempoInicial;
    let intervalo;

    function actualizarTiempo() {
        tiempo++;
        tiempoBombaEl.textContent = tiempo + " s";
    }

    function crearBurbuja() {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");
        bubble.style.left = Math.random() * 180 + "px";
        bubble.style.animationDuration = Math.random() * 2 + 2 + "s";

        liquido.appendChild(bubble);
        setTimeout(() => {
            bubble.remove();
        }, 4000);
    }

    function encenderAnimacion() {
        liquido.style.transition = "height 0.5s ease-in-out";
        liquido.style.height = "100%";
        tank.classList.add("active");
        intervalo = setInterval(() => {
            actualizarTiempo();
            crearBurbuja();
        }, 1000);
    }

    function apagarAnimacion() {
        liquido.style.transition = "height 0.5s ease-in-out";
        liquido.style.height = "0%";
        tank.classList.remove("active");
        clearInterval(intervalo);
    }

    if (bombaEncendida) {
        encenderAnimacion();
    } else {
        apagarAnimacion();
    }
});
