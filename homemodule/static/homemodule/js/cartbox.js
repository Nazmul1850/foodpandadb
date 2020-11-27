var totalprice = 0;
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
  console.log(memory);
  for(m in memory) {
    //console.log(memory[m].name);
    foodlist.push(new FoodCart(memory[m].id,memory[m].name,memory[m].price,memory[m].amount));
    totalprice += memory[m].price;
  }
});

// NOTE: make new food item
function foodObject(id, name, price) {
  var amountcheck = 0;
  for(const cart of foodlist) {
    if (cart.id == id) {
      console.log("increased");
      cart.increaseAmount();
      totalprice += price;
      amountcheck =1;
      break;
    }
  }
  if (amountcheck == 0) {
    foodlist.push(new FoodCart(id,name,price,1));
    totalprice += price;
  }
}
// NOTE: Delete a item
function deleteCart(id){
  //alert("delete!!" + name + price);
  foodlist.forEach((item, i, object) => {
    if(item.id == id ) {
      if(item.amount==1){
        totalprice -= item.price;
        object.splice(i,1);
      }
      else{
        item.decreaseAmount();
        totalprice -= item.price;
      }
    }
    //btnclick.updateol.call();
  });
  btnclick.updateol.call();
}

// NOTE: Refresh ul li items in cart
$(document).ready(function() {
  var b2 = $("button.plus");
  btnclick = {
    updateol: function() {
    const renderHook = document.getElementById('showcart');
    const cartlist = document.getElementById('ol-cart-list');
    var items = document.querySelectorAll("#ol-cart-list li");
    //console.log(items);
    for(var i=0; i<items.length; i++) {
      //console.log(items[i]);
      items[i].parentNode.removeChild(items[i]);
    }
    for (const cart of foodlist) {
        const cartitem = document.createElement('li');
        cartitem.classname = 'cart-item';
        //console.log(cart.name);
        cartitem.innerHTML = `
        <div class="cartitem-content">
            <span>${cart.name} (${cart.amount})</span>
            <span>/${cart.price}</span>
            <button type="button" id = "minus" name="minus" onclick="deleteCart(${cart.id})">-</button>
          </div>
        `;
        cartlist.append(cartitem);
    }
    const cost = document.getElementById('total-price');
    cost.innerHTML = `
        <span>Total :${totalprice}</span>
    `;
    cartlist.append(cost);
    renderHook.append(cartlist);
    sessionStorage.setItem("foodlist", JSON.stringify(foodlist));
  }
}
  btnclick.updateol.call();
  b2.on('click', btnclick.updateol);

});
