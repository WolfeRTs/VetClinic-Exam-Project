const hintBox = document.querySelector(".hint-box");
const description = document.querySelector(".hint-content");

const handleMouseOver = (container, event) => {
    const item = event.target.closest(".item-tag");
    if (item && container.contains(item)) {
        description.textContent = item.getAttribute("data-tag-item") || "";
        const rect = item.getBoundingClientRect();

        hintBox.style.top = `${window.scrollY + rect.bottom + 5}px`;
        hintBox.style.left = `${rect.left}px`;
        hintBox.classList.remove("hidden");
    }
};

const handleMouseOut = (container, event) => {
    const item = event.target.closest(".item-tag");
    if (item && container.contains(item)) {
        hintBox.classList.add("hidden");
    }
};

[...document.querySelectorAll(".service-tags, .medicine-tags")].forEach((container) => {
    container.addEventListener("mouseover", (event) => handleMouseOver(container, event));
    container.addEventListener("mouseout", (event) => handleMouseOut(container, event));
});