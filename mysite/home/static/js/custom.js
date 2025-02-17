document.addEventListener("DOMContentLoaded", function() {
  var acc = document.getElementsByClassName("accordion"); 
  console.log("Accordion elements:", acc); // 요소가 잘 잡히는지 확인

  for (let i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function() {
          this.classList.toggle("active");
          var panel = this.nextElementSibling;
          if (panel.style.display === "block") {
              panel.style.display = "none";
          } else {
              panel.style.display = "block";
          }
      });
  }
});

console.log("custom.js loaded");
console.log(document.getElementsByClassName("accordion"));
