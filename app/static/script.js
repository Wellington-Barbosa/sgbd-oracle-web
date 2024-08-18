function switchPasswordType() {
    let passInput = document.getElementById("password");
    let passIcon = document.getElementById("passIcon");
    if (passInput.type === "password") {
        passInput.type = "text";
        passIcon.classList.remove("bi-eye");
        passIcon.classList.add("bi-eye-slash");
    } else {
        passInput.type = "password";
        passIcon.classList.remove("bi-eye-slash");
        passIcon.classList.add("bi-eye");
    }
}