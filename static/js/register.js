const usernameField = document.querySelector("#usernameField");
const usernamefeedbackArea = document.querySelector(".usernamefeedbackArea");
const emailField = document.querySelector("#emailField");
const emailfeedbackArea = document.querySelector(".emailfeedbackArea");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submit-btn");

const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "SHOW") {
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "SHOW";
    passwordField.setAttribute("type", "password");
  }
};

showPasswordToggle.addEventListener("click", handleToggleInput);

emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  emailField.classList.remove("is-invalid");
  emailfeedbackArea.style.display = "none";

  if (emailVal.length > 0) {
    fetch("/authentication/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.email_error) {
          submitBtn.disabled = true;
          emailField.classList.add("is-invalid");
          emailfeedbackArea.style.display = "block";
          emailfeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;
  usernameField.classList.remove("is-invalid");
  usernamefeedbackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.username_error) {
          submitBtn.disabled = true;
          usernameField.classList.add("is-invalid");
          usernamefeedbackArea.style.display = "block";
          usernamefeedbackArea.innerHTML = `<p>${data.username_error}</p>`;
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });
  }
});
