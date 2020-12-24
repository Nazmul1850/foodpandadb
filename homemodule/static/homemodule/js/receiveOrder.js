$(document).ready(function() {
        document.getElementById("order-receive").addEventListener("click",function() {
          console.log("Receive called");
          document.querySelector(".popup-review").style.display = "flex";
          $.ajax({
              url:"http://localhost:8000/completeOrder/",
              type:"POST",
          })
          .done(function(response){
              console.log(response);
          })
          .fail(function(){
             console.log("Error Occured");
          });
        });
        document.getElementById("close").addEventListener("click",function() {
          console.log("close called");
          document.querySelector(".popup-review").style.display = "none";
        });
});
