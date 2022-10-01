const days = document.querySelectorAll(".day");

for (let day of days) {
    day.addEventListener("click", function(event) {
        event.target.classList.add("class", "completed");
    });
}