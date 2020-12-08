$(document).ready(function(){
            $(document).on("dblclick",".editable",function(){
                var value=$(this).text();
                var data_type=$(this).data("type");
                var input_type="number";
                var input="<input type='"+input_type+"' class='input-data' value='"+value+"' class='form-control'>";
                $(this).html(input);
                $(this).removeClass("editable")
            });
            $(document).on("dblclick",".editable-d",function(){
                var value=$(this).text();
                var data_type=$(this).data("type");
                var input_type="date";
                var input="<input type='"+input_type+"' class='input-data' value='"+value+"' class='form-control'>";
                $(this).html(input);
                $(this).removeClass("editable food")
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
                $.ajax({
                    url:"http://localhost:8000/saveoffer/",
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

function addRowOffer(res_id) {
    const renderHook = document.getElementById('new-row-offer');
    renderHook.innerHTML = `
      <td class="neweditable" data-id="-1"><input type="number" id="new-input-data-dpct" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="number" id="new-input-data-maxd" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="date" id="new-input-data-expd" class="form-control"></td>
      <td class="neweditable" data-id="-1"><input type="date" id="new-input-data-startd" class="form-control"></td>
      <td class="neweditableB" data-id="-1"><a class="btn btn-sm btn-success" href="#" onclick="add_newOffer(${res_id})">Update</a></td>
    `;
}

function add_newOffer(res_id) {
  var discount_pct = document.getElementById("new-input-data-dpct").value;
  var max_discount = document.getElementById("new-input-data-maxd").value;
  var expiry = document.getElementById("new-input-data-expd").value;
  var start = document.getElementById("new-input-data-startd").value;
  $.ajax({
      url:"http://localhost:8000/addnewoffer/",
      type:"POST",
      data:{discount_pct:discount_pct,max_discount:max_discount,expiry:expiry,res_id:res_id,start:start},
  })
  .done(function(response){
      console.log(response);
  })
  .fail(function(){
     console.log("Error Occured");
  });
}
