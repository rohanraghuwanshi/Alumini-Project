var swiper = new Swiper('.swiper-container', {
    cssMode: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination'
    },
    mousewheel: true,
    keyboard: true,
});

const toggler = document.querySelector(".menu_toggler");
const menu = document.querySelector(".menu");

toggler.addEventListener("click", () => {
    toggler.classList.toggle("active");
    menu.classList.toggle("active");
});