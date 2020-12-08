$(document).ready(function() {
        document.getElementById("order-receive").addEventListener("click",function() {
          console.log("Receive called");
          document.querySelector(".popup-review").style.display = "flex";
        });
        document.getElementById("close").addEventListener("click",function() {
          console.log("close called");
          document.querySelector(".popup-review").style.display = "none";
        });
});
