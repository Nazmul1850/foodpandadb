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



            // NOTE: food
});
// $(document).ready(function() {
//    // Stuff to do as soon as the DOM is ready
//    $(document).on("dblclick",".editable food",function(){
//        var value=$(this).text();
//        var data_type=$(this).data("type");
//        var input_type="text";
//        var input="<input type='"+input_type+"' class='input-data-food' value='"+value+"' class='form-control'>";
//        $(this).html(input);
//        $(this).removeClass("editable food")
//    });
//
//    $(document).on("blur",".input-data-food",function(){
//        var value=$(this).val();
//        var td=$(this).parent("td");
//        $(this).remove();
//        td.html(value);
//        td.addClass("editable food");
//        var type=td.data("type");
//        console.log(value);
//        sendToServer2(td.data("id"),value,type);
//    });
//    $(document).on("keypress",".input-data-food",function(e){
//       var key=e.which;
//       if(key==13){
//           var value=$(this).val();
//           var td=$(this).parent("td");
//           $(this).remove();
//           td.html(value);
//           td.addClass("editable food");
//           var type=td.data("type");
//           sendToServer2(td.data("id"),value,type);
//       }
//   });
//
//   function sendToServer2(id,value,type){
//        //console.log(id);
//        console.log(value);
//        console.log(type);
//        $.ajax({
//            url:"http://localhost:8000/savefood/",
//            type:"POST",
//            data:{id:id,type:type,value:value},
//        })
//        .done(function(response){
//            console.log(response);
//        })
//        .fail(function(){
//           console.log("Error Occured");
//        });
//
//    }
// });


function deleteRes(id) {
  alert("Are You Sure You Want To Delete This Restaurant")
}
function addfood(res_id) {
  //alert("Add Food" + res_id);
  $.ajax({
      url:"http://localhost:8000/foodcall/",
      type:"POST",
      data:{res_id:res_id},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
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
      <td class="neweditable" data-id="-1"><a class="btn btn-sm btn-success" href="{% url 'restaurant' %}" onclick="newValue()">Update</a></td>
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

// function addRowFood(res_id) {
//     const renderHook = document.getElementById('new-row-food');
//     renderHook.innerHTML = `
//       <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-name" class="form-control"></td>
//       <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-cuisine" class="form-control"></td>
//       <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-price" class="form-control"></td>
//       <td class="neweditable" data-id="-1"><input type="text" id="new-input-data-avl" class="form-control"></td>
//       <td class="neweditableB" data-id="-1"><a class="btn btn-sm btn-success" href="#" onclick="add_newfood_of_res(${res_id})">Update</a></td>
//     `;
// }
//
// function add_newfood_of_res(res_id) {
//   console.log("resss" + res_id);
//   var name = document.getElementById("new-input-data-name").value;
//   var cuisine = document.getElementById("new-input-data-cuisine").value;
//   var price = document.getElementById("new-input-data-price").value;
//   var avl = document.getElementById("new-input-data-avl").value;
//   console.log(name + cuisine + price + avl);
//   $.ajax({
//       url:"http://localhost:8000/addnewfood/",
//       type:"POST",
//       data:{res_id:res_id,name:name,cuisine:cuisine,price:price,avl:avl},
//   })
//   .done(function(response){
//       console.log(response);
//   })
//   .fail(function(){
//      console.log("Error Occured");
//   });
// }
