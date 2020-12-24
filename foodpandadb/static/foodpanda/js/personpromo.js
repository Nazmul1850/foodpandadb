function addRowPersonPromo(id) {
  const renderHook = document.getElementById('new-row-person-promo');
  renderHook.innerHTML = `
    <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-code" class="form-control"></td>
    <td class="neweditableB" data-id="-1"><a class="btn btn-sm btn-success" href="#" onclick="add_newPersonPromo('${id}')">Update</a></td>
  `;
}
function add_newPersonPromo(id) {
  console.log("Update person Called" + id);
  var code = document.getElementById("new-input-data-code").value;
  $.ajax({
      url:"http://localhost:8000/addnewpersonpromo/",
      type:"POST",
      data:{code:code,id:id},
  })
  .done(function(response){
      console.log(response);
      alert(response.success);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
