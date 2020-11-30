$(document).ready(function(){
            $(document).on("dblclick",".editable",function(){
                var value=$(this).text();
                var data_type=$(this).data("type");
                var input_type="text";
                var input="<input type='"+input_type+"' class='input-data' value='"+value+"' class='form-control'>";
                $(this).html(input);
                $(this).removeClass("editable")
            });

            $(document).on("blur",".input-data",function(){
                var value=$(this).val();
                var td=$(this).parent("td");
                $(this).remove();
                td.html(value);
                td.addClass("editable");
                var type=td.data("type");
                sendToServer(td.data("id"),value,type);
            });
            $(document).on("keypress",".input-data",function(e){
               var key=e.which;
               if(key==13){
                   var value=$(this).val();
                   var td=$(this).parent("td");
                   $(this).remove();
                   td.html(value);
                   td.addClass("editable");
                   var type=td.data("type");
                   sendToServer(td.data("id"),value,type);
               }
           });

           function sendToServer(id,value,type){
                console.log(id);
                console.log(value);
                console.log(type);
                $.ajax({
                    url:"http://localhost:8000/saverestaurant/",
                    type:"POST",
                    data:{id:id,type:type,value:value},
                })
                .done(function(response){
                    console.log(response);
                })
                .fail(function(){
                   console.log("Error Occured");
                });

            }
});

function deleteRes(id) {
  alert("Are You Sure You Want To Delete This Restaurant")
}

function addRow() {
    const renderHook = document.getElementById('new-row');
    renderHook.innerHTML = `
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-id" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-name" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-location" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-phone" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-email" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-opening" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-closing" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-image" class="form-control"></td>
      <td class="neweditable" data-id="-1"><a class="btn btn-sm btn-success" href="#" onclick="newValue()">Update</a></td>
    `;
}
function newValue() {
  var id = document.getElementById("new-input-data-id").value;
  var name = document.getElementById("new-input-data-name").value;
  var location = document.getElementById("new-input-data-location").value;
  var phone = document.getElementById("new-input-data-phone").value;
  var email = document.getElementById("new-input-data-email").value;
  var opening = document.getElementById("new-input-data-opening").value;
  var closing = document.getElementById("new-input-data-closing").value;
  var image = document.getElementById("new-input-data-image").value;
  console.log("->" + id + name + location + phone + email + opening + closing + image);
  $.ajax({
      url:"http://localhost:8000/addnewrestaurant/",
      type:"POST",
      data:{id:id,name:name,location:location,phone:phone,email:email,opening:opening,closing:closing,image:image},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
