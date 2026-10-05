let total = 0;

function addToCart(product, price) {

    let cartItems = document.getElementById("cart-items");

    let li = document.createElement("li");
    li.textContent = `${product} - ₹${price}`;

    cartItems.appendChild(li);

    total += price;

    document.getElementById("total").textContent = total;
}