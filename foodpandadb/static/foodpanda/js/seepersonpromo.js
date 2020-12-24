function addpromo(id) {
  console.log("Person" + id);
  $.ajax({
      url:"http://localhost:8000/personpromo/",
      type:"POST",
      data:{id:id},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
