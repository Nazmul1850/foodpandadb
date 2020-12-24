
var foodlist = [];
var btnclick;


// NOTE: Food Class
class FoodCart {
  name = 'DEFAULT';
  id;
  price;
  amount;
  constructor(id, name, price,amount) {
    this.id = id;
    this.name = name;
    this.price = price;
    this.amount = amount;
  }
  increaseAmount() {
    this.amount += 1;
  }
  decreaseAmount() {
    this.amount -= 1;
  }
}


// NOTE: update foodlist from session data
$(document).ready(function(){
  var memory = JSON.parse(sessionStorage.getItem("foodlist"));
  for(m in memory) {
    //console.log(memory[m].name);
    foodlist.push(new FoodCart(memory[m].id,memory[m].name,memory[m].price,memory[m].amount));
  }
});


// NOTE: make new food item
function checkRes(res_name,id, name, price) {
  console.log(foodlist.length);
  if (sessionStorage.getItem("res_name") == null || (foodlist.length == 0)) {
    sessionStorage.setItem("res_name",res_name);
    foodObject(id,name,price);
    //const res_check = document.getElementById('res-check');
    //res_check.innerHTML = `
    //`;
    //console.log("Notun res");
  }
  else {
    var pre_res = sessionStorage.getItem("res_name");
    //console.log("pre_res->" + pre_res);
    if (res_name == pre_res) {
      foodObject(id,name,price);
      //console.log("Milse");
    }
    else {
      //console.log("mile nai");
      const res_check = document.getElementById('res-check');
      res_check.innerHTML = `
        <span> Please Order From a Single Restaurant Or Clear your cart..</span>
      `;
    }
  }
}

function foodObject(id, name, price) {
  var amountcheck = 0;
  for(const cart of foodlist) {
    if (cart.id == id) {
      console.log("increased");
      cart.increaseAmount();
      amountcheck =1;
      break;
    }
  }
  if (amountcheck == 0) {
    foodlist.push(new FoodCart(id,name,price,1));
  }
}
// NOTE: Delete a item
function deleteCart(id){
  //alert("delete!!" + name + price);
  foodlist.forEach((item, i, object) => {
    if(item.id == id ) {
      if(item.amount==1){
        object.splice(i,1);
      }
      else{
        item.decreaseAmount();
      }
    }
    //btnclick.updateol.call();
  });
  btnclick.updateol.call();
}

// NOTE: Refresh ul li items in cart
$(document).ready(function() {
  var b2 = $(".plus");
  btnclick = {
    updateol: function() {
    //const renderHook = document.getElementById('showcart');
    console.log('called');
    //const cartlist = document.getElementById('ol-cart-list');
    //var items = document.querySelectorAll("#ol-cart-list li");
    //console.log(items);
    //for(var i=0; i<items.length; i++) {
      //console.log(items[i]);
      //items[i].parentNode.removeChild(items[i]);
    //}
    var total = 0;
    var cartamount = 0;
    for (const cart of foodlist) {
        cartamount += 1;
        //const cartitem = document.createElement('li');
        //cartitem.classname = 'cart-item';
        total += cart.amount * cart.price
        //console.log(cart.name);
        // cartitem.innerHTML = `
        // <div class="cartitem-content">
        //     <span>${cart.name} (${cart.amount})</span>
        //     <span>/${cart.price}</span>
        //     <button type="button" id = "minus" name="minus" onclick="deleteCart(${cart.id})">-</button>
        //   </div>
        // `;
        // cartlist.append(cartitem);
    }
    // const cost = document.getElementById('total-price');
    // cost.innerHTML = `
    //     <span>Total :${total}</span>
    // `;
    // cartlist.append(cost);
    // renderHook.append(cartlist);
    sessionStorage.setItem("foodlist", JSON.stringify(foodlist));
    const cart = document.getElementById('cart_icon');
    var presup = document.getElementById('cart_sup');
    presup.remove();
    const sup = document.createElement('sup');
    sup.id = 'cart_sup'
    sup.innerHTML = `
       <b><span style="color:red">${cartamount}</span></b>
    `;
    cart.append(sup);

  }
}
  btnclick.updateol.call();
  b2.on('click', btnclick.updateol);

});
