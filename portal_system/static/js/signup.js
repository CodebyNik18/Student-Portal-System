const roleOptions = document.querySelectorAll(".role-option");
const teacherSection = document.getElementById("teacherSection");
const roleInput = document.getElementById("roleInput");

roleOptions.forEach(option => {
    option.addEventListener("click", () => {

        roleOptions.forEach(o => o.classList.remove("active"));
        option.classList.add("active");

        const selectedRole = option.dataset.role;

        roleInput.value = selectedRole;

        // Toggle teacher section
        if (selectedRole === "teacher") {
            teacherSection.style.display = "block";
        } else {
            teacherSection.style.display = "none";
        }
    });
});
