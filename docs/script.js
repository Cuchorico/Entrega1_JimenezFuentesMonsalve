document.addEventListener('DOMContentLoaded', (event) => {
    let image_container_2 = document.getElementsByClassName("image-container-2")[0];

    window.onscroll = function () {
        image_container_2.classList.add("aparecer-image-container-2");

        var distancia = window.innerHeight - image_container_2.getBoundingClientRect().top;

        if (distancia >= 511) {
            image_container_2.classList.add("aparecer-image-container-2");
        }

        console.log(distancia);
    };
});