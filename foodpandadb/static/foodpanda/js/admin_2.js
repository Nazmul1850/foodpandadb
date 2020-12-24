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
                console.log(value);
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
                    url:"http://localhost:8000/savefood/",
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

function addRowFood(res_id) {
    const renderHook = document.getElementById('new-row-food');
    renderHook.innerHTML = `
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-name" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-cuisine" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-price" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-avl" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-img" class="form-control"></td>
      <td class="neweditableB" data-id="-1"><a class="btn btn-sm btn-success" href="#" onclick="add_newfood_of_res(${res_id})">Update</a></td>
    `;
}

function add_newfood_of_res(res_id) {
  console.log("resss" + res_id);
  var name = document.getElementById("new-input-data-name").value;
  var cuisine = document.getElementById("new-input-data-cuisine").value;
  var price = document.getElementById("new-input-data-price").value;
  var avl = document.getElementById("new-input-data-avl").value;
  var img = document.getElementById("new-input-data-img").value;
  console.log(name + cuisine + price + avl);
  $.ajax({
      url:"http://localhost:8000/addnewfood/",
      type:"POST",
      data:{res_id:res_id,name:name,cuisine:cuisine,price:price,avl:avl,img:img},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}


function updateOffer() {
  $.ajax({
      url:"http://localhost:8000/updateOffer/",
      type:"POST",
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
