var swiper = new Swiper('.swiper-container', {
    cssMode: true,
    mousewheel: false,
    keyboard: true,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    pagination: {
        el: '.swiper-pagination'
    },
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
    },
});

var swiper = new Swiper('.message-swiper-container', {
    spaceBetween: 30,
    centeredSlides: true,
    mousewheelControl: false,
    keyboard: true,
    autoplay: {
        delay: 8000,
        disableOnInteraction: false,
    },
});
