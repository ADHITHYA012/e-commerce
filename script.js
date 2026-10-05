let cartCount = 0;

function addToCart(productName) {

    cartCount++;

    document.getElementById("cart-count").innerText = cartCount;

    alert(productName + " added to cart!");
}

function buyNow(productName) {

    alert("Buying: " + productName);

    window.location.href = "/success";
}
