document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".news-carousel");
    const prevButton = document.querySelector(".prev-button");
    const nextButton = document.querySelector(".next-button");
    let currentIndex = 0;
    function slideLeft() {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = 0;
        }
        updateCarousel();
    }
    function slideRight() {
        currentIndex++;
        const numNewsItems = document.querySelectorAll(".news-item").length;
        if (currentIndex >= numNewsItems - 2) {
            currentIndex = numNewsItems - 3;
        }
        updateCarousel();
    }
    function updateCarousel() {
        const itemWidth = document.querySelector(".news-item").offsetWidth;
        const newPosition = -currentIndex * (itemWidth + 20);
        carousel.style.transform = `translateX(${newPosition}px)`;
    }
    prevButton.addEventListener("click", slideLeft);
    nextButton.addEventListener("click", slideRight);
});
