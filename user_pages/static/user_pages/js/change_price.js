let additionalOptions = document.querySelectorAll(".check");
let fullPrice = document.querySelector("#fullPrice");
let hiddenValue = document.querySelector("#hiddenValue");

let listCheckedOptions = Array();

function sumPrice() {
    let addPrice = 0;
    let price = parseInt(document.querySelector("#priceProduct").textContent.split(" ")[0]);
    listCheckedOptions = Array();
    additionalOptions.forEach(function (additionalOptions) {
        if (additionalOptions.checked == true) {
            let addicionalOptionPrice = parseInt(additionalOptions.value);
            addPrice += addicionalOptionPrice;

            let parentDiv = additionalOptions.closest("div");

            let optionsPk = parentDiv.querySelector(".options-pk")

            listCheckedOptions.push(optionsPk.value);
        }
    });
    let fullSumPrice = addPrice + price;
    fullPrice.textContent = `${String(fullSumPrice)}`;
    // hiddenValue.value = `${String(fullSumPrice)}`;
};

additionalOptions.forEach(function (additionalOptions) {
    additionalOptions.addEventListener("click", function () {
        sumPrice();
    });
});

document.addEventListener('DOMContentLoaded', sumPrice());

$(document).ready(function () {
    $(".addToCart").on("submit", function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: $(this).action,
            data: { csrfmiddlewaretoken: document.getElementsByName("csrfmiddlewaretoken")[0].value,
                    "product_pk":document.getElementsByName("product_pk")[0].value,
                    "listCheckedOptions":listCheckedOptions,
                    }
                    
        });
    });
});