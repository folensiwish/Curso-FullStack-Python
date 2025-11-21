    document.addEventListener("DOMContentLoaded", () => {
        const scrollToTopBtn = document.getElementById("scrollToTopBtn");
        const scrollThreshold = 200; // Adjust as needed

        const toggleScrollToTopBtn = () => {
            if (window.scrollY > scrollThreshold) {
                scrollToTopBtn.classList.add("show");
            } else {
                scrollToTopBtn.classList.remove("show");
            }
        };

        const scrollToTop = () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        };

        window.addEventListener("scroll", toggleScrollToTopBtn);
        scrollToTopBtn.addEventListener("click", scrollToTop);
    });