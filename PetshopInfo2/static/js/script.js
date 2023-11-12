'use strict';



/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
}



/**
 * navbar toggle
 */

const navToggler = document.querySelector("[data-nav-toggler]");
const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");

const toggleNavbar = function () {
  navbar.classList.toggle("active");
  navToggler.classList.toggle("active");
}

addEventOnElem(navToggler, "click", toggleNavbar);


const closeNavbar = function () {
  navbar.classList.remove("active");
  navToggler.classList.remove("active");
}

addEventOnElem(navbarLinks, "click", closeNavbar);



/**
 * active header when window scroll down to 100px
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElemOnScroll = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

let carritoCount = 0; // Inicializa el contador del carrito
// let carritoCount = {{ carritoCount|default:0 }};


// Función para actualizar el número en el carrito
function updateCarritoCount(count) {
    const carritoElement = document.getElementById("carrito");
    const badgeElement = carritoElement.querySelector("span.badge");
    badgeElement.textContent = count;
}

// Función para obtener la cantidad actualizada del carrito desde el servidor
function fetchCartCount() {
    fetch("get_cart_count")  // Reemplaza con la URL correcta
        .then(response => response.json())
        .then(data => {
            if (data.carritoCount !== undefined) {
                carritoCount = data.carritoCount;
                updateCarritoCount(carritoCount);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Agregar un evento de clic a los botones "Add to cart"
const addToCartButtons = document.querySelectorAll(".btn-add-to-cart");
addToCartButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Realizar la lógica para agregar al carrito aquí

        // Después de agregar al carrito, obtener la cantidad actualizada
        fetchCartCount();
    });
});

// Llamada inicial para obtener la cantidad al cargar la página
fetchCartCount();


// // Función para actualizar el número en el carrito
// function updateCarritoCount() {
//     const carritoElement = document.getElementById("carrito");
//     const badgeElement = carritoElement.querySelector("span.badge");
//     badgeElement.textContent = carritoCount;
//     // carritoLink.href = carritoCount > 0 ? "{% url 'carritooo' %}" : "#";
// }



// // Agregar un evento de clic a los botones "Add to cart"
// const addToCartButtons = document.querySelectorAll(".btn-add-to-cart");
// addToCartButtons.forEach(button => {
//     button.addEventListener("click", () => {
//         carritoCount++; // Aumenta el contador del carrito al hacer clic
//         updateCarritoCount(); // Actualiza el número en el carrito
//         // event.preventDefault();
//         // fetch(button.closest("form").action, {
//         //   method: "POST",
//         //   body: new FormData(button.closest("form")),
//         // })
//         // .then(response => response.json())
//         // .then(data => {
//         //     if (data.success) {
//         //         carritoCount = data.carritoCount; // Actualiza el contador del carrito
//         //         updateCarritoCount(); // Actualiza el número en el carrito
//         //     }
//         // })
//         // .catch(error => {
//         //     console.error('Error:', error);
//         // });
//     });
// });

// Agregar un evento de clic al botón del carrito
const carritoBtn = document.getElementById("carrito");
carritoBtn.addEventListener("click", () => {
  const cartUrl = carritoBtn.getAttribute("data-cart-url");
    // Agrega aquí la lógica para dirigir al usuario a la vista del carrito
  window.location.href = cartUrl;
});












function changeColor(element) {
  // Cambia el color cuando el mouse entra
  element.style.color = "#ff4500"; // Puedes cambiar el color a tu elección
}

function restoreColor(element) {
  // Restaura el color original cuando el mouse sale
  element.style.color = ""; // Esto restaura el color original del CSS
}

addEventOnElem(window, "scroll", activeElemOnScroll);