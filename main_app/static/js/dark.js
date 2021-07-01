// DAY NIGHT JS

var checkbox = document.querySelector("input[name=mode]");

checkbox.addEventListener("change", function () {
   if (this.checked) {
      trans();
      document.documentElement.setAttribute("data-theme", "dark");
   } else {
      trans();
      document.documentElement.setAttribute("data-theme", "light");
   }
});

let trans = () => {
   document.documentElement.classList.add("transition");
   window.setTimeout(() => {
      document.documentElement.classList.remove("transition");
   }, 1000);
};


// REGISTER LOGIN JS

var login = document.getElementById("box");
var register = document.getElementById("boxr");

function LOGIN(){
  register.style.top = "-500%";
  login.style.top = "50%";
}

function REGISTER(){
  login.style.top = "-500%";
  register.style.top = "50%";
}
