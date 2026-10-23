
document.addEventListener("DOMContentLoaded", function () {

    
    const searchForm = document.querySelector("#searchForm");

    if (searchForm) {
        searchForm.addEventListener("submit", function (event) {
            const searchInput = searchForm.querySelector(
                'input[name="search"]'
            );

            if (searchInput) {
                searchInput.value = searchInput.value.trim();
            }
        });
    }

 
    const addToCartForms = document.querySelectorAll(".add-to-cart-form");

    addToCartForms.forEach(function (form) {
        form.addEventListener("submit", function () {
            const button = form.querySelector("button[type='submit']");

            if (button) {
                button.disabled = true;
                button.textContent = "Adding...";
            }
        });
    });

   
    const buyNowForms = document.querySelectorAll(".buy-now-form");

    buyNowForms.forEach(function (form) {
        form.addEventListener("submit", function () {
            const button = form.querySelector("button[type='submit']");

            if (button) {
                button.disabled = true;
                button.textContent = "Processing...";
            }
        });
    });
   
    const removeForms = document.querySelectorAll(".remove-from-cart-form");

    removeForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = confirm(
                "Are you sure you want to remove this product from your cart?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // Checkout Confirmation
    const checkoutForm = document.querySelector("#checkoutForm");

    if (checkoutForm) {
        checkoutForm.addEventListener("submit", function (event) {
            const confirmed = confirm(
                "Are you sure you want to proceed with checkout?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    }

    // Mobile Navigation
    const menuButton = document.querySelector("#menuButton");
    const navigation = document.querySelector("#navigation");

    if (menuButton && navigation) {
        menuButton.addEventListener("click", function () {
            navigation.classList.toggle("active");

            const isExpanded = navigation.classList.contains("active");
            menuButton.setAttribute("aria-expanded", isExpanded);
        });
    }

    // Back to Top Button
    const backToTop = document.querySelector("#backToTop");

    if (backToTop) {
        window.addEventListener("scroll", function () {
            backToTop.style.display =
                window.scrollY > 300 ? "block" : "none";
        });

        backToTop.addEventListener("click", function () {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }

});

