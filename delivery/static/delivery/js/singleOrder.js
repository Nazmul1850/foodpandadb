
function completeOrder(id) {
  console.log("complete called");
  $.ajax({
      url:"http://localhost:8000/completeDelivery/",
      type:"POST",
      data:{'id':id},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
