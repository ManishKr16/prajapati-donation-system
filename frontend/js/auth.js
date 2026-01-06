// REGISTER
const registerForm = document.getElementById("registerForm");
if (registerForm) {
  registerForm.onsubmit = (e) => {
    e.preventDefault();
    alert("Registration successful (dummy)");
    window.location.href = "login.html";
  };
}

// LOGIN
const loginForm = document.getElementById("loginForm");
if (loginForm) {
  loginForm.onsubmit = (e) => {
    e.preventDefault();

    // dummy user data
    localStorage.setItem("user_id", "USER123");
    localStorage.setItem("name", "Demo User");
    localStorage.setItem("mobile", "9999999999");

    alert("Login successful");
    window.location.href = "donate.html";
  };
}
