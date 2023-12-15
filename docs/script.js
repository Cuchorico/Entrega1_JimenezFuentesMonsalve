document.addEventListener('DOMContentLoaded', (event) => {
    let image_container_2 = document.getElementsByClassName("image-container-2")[0];

    window.onscroll = function () {
        image_container_2.classList.add("aparecer-image-container-2");

        var revealpoint = window.innerHeight - image_container_2.getBoundingClientRect().top;

        if (revealpoint = 700) {
            image_container_2.classList.add("aparecer-image-container-2");
        }

        console.log(revealpoint);
    };
});


document.addEventListener('DOMContentLoaded', (event) => {
    let image_container_3 = document.getElementsByClassName("image-container-3")[0];

    window.onscroll = function () {
        image_container_2.classList.add("aparecer-image-container-3");

        var revealpoint = window.innerHeight - image_container_3.getBoundingClientRect().top;

        if (revealpoint = 1200) {
            image_container_2.classList.add("aparecer-image-container-3");
        }

        console.log(revealpoint);
    };
});