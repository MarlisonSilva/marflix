const icon_house = document.getElementById("icon_house");
const anchor_icon_house = document.getElementById("anchor_icon_house");

anchor_icon_house.addEventListener("mouseover", function() {
    icon_house.classList.remove("bi-house");
    icon_house.classList.add("bi-house-fill");
});

anchor_icon_house.addEventListener("mouseout", function() {
    icon_house.classList.remove("bi-house-fill");
    icon_house.classList.add("bi-house");
});

const icon_plus = document.getElementById("icon_plus");
const anchor_icon_plus = document.getElementById("anchor_icon_plus");

anchor_icon_plus.addEventListener("mouseover", function() {
    icon_plus.classList.remove("bi-plus-circle");
    icon_plus.classList.add("bi-plus-circle-fill");
});

anchor_icon_plus.addEventListener("mouseout", function() {
    icon_plus.classList.remove("bi-plus-circle-fill");
    icon_plus.classList.add("bi-plus-circle");
});

const close_modals = document.querySelectorAll(".close_modal");
const open_modals = document.querySelectorAll(".open_modal");

close_modals.forEach(close_modal => {
    close_modal.addEventListener("click", () => {
        close_modal.closest(".modal").classList.add("hidden");
    });
});

open_modals.forEach(open_modal => {
    open_modal.addEventListener("click", () => {
        const targetModal = document.querySelector(open_modal.getAttribute("data-target"));
        if (targetModal) {
            targetModal.classList.remove("hidden");
        }
    });
});