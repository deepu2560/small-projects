let pswrd = document.getElementById("pswrd");
let togglebtn = document.getElementById("toggleBtn");

let lowercase = document.getElementById("lower");
let uppercase = document.getElementById("upper");
let digit = document.getElementById("number");
let specialChar = document.getElementById("special");
let minLength = document.getElementById("length");

function checkPassword(data) {
  const lower = new RegExp("(?=.*[a-z])");
  const upper = new RegExp("(?=.*[A-Z])");
  const number = new RegExp("(?=.*[0-9])");
  const special = new RegExp("(?=.*[!@#$^$*])");
  const length = new RegExp("(?=.{8,})");

  if (lower.test(data)) {
    lowercase.classList.add("valid");
  } else {
    lowercase.classList.remove("valid");
  }

  if (upper.test(data)) {
    uppercase.classList.add("valid");
  } else {
    uppercase.classList.remove("valid");
  }

  if (number.test(data)) {
    digit.classList.add("valid");
  } else {
    digit.classList.remove("valid");
  }

  if (special.test(data)) {
    specialChar.classList.add("valid");
  } else {
    specialChar.classList.remove("valid");
  }

  if (length.test(data)) {
    minLength.classList.add("valid");
  } else {
    minLength.classList.remove("valid");
  }
}

togglebtn.onclick = function () {
  if (pswrd.type === "password") {
    pswrd.setAttribute("type", "text");
    togglebtn.classList.add("hide");
  } else {
    pswrd.setAttribute("type", "password");
    togglebtn.classList.remove("hide");
  }
};
