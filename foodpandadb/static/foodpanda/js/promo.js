function addRowPromo() {
    const renderHook = document.getElementById('new-row-promo');
    renderHook.innerHTML = `
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-code" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="number" id="new-input-data-discount" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="date" id="new-input-data-start" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="date" id="new-input-data-end" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-status" class="form-control"></td>
      <td class="neweditableB" data-id="-1"><a class="btn btn-sm btn-success" href="#" onclick="add_newPromo()">Update</a></td>
    `;
}

function add_newPromo() {
  console.log("Update Called");
  var code = document.getElementById("new-input-data-code").value;
  var discount = document.getElementById("new-input-data-discount").value;
  var start = document.getElementById("new-input-data-start").value;
  var end = document.getElementById("new-input-data-end").value;
  var status = document.getElementById("new-input-data-status").value;
  $.ajax({
      url:"http://localhost:8000/addnewpromo/",
      type:"POST",
      data:{code:code,discount:discount,start:start,end:end,status:status},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}

function updatePromo() {
  console.log("updatepromo");
  $.ajax({
      url:"http://localhost:8000/updateprpmo/",
      type:"POST",
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
