
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
  btnclick.updateol.call();
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
  var b2 = $("a.cart_icon");
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
    var total = 0;
    var cartamount = 0;
    for (const cart of foodlist) {
        cartamount += 1;
        const cartitem = document.createElement('li');
        cartitem.classname = 'cart-item';
        total += cart.amount * cart.price
        //console.log(cart.name);
        cartitem.innerHTML = `
        <div class="cartitem-content">
        <ul class="horizontal">
           <li><span id="cart-name">${cart.name}</span></li>
          <li><span id="cart-amount">(${cart.amount})</span><span id="cart-price">/${cart.price}</span></li>
          <li><span id="cart-option">
                 <button type="button" id = "inc" class="cart-button" onclick="foodObject('${cart.id}','${cart.name}','${cart.price}')">
                      +</button>
                 <button type="button" id = "dec" class="cart-button" onclick="deleteCart(${cart.id})">-</button>
              </span>
          </li>
           <!-- <li><button type="button" id = "inc" name="minus" onclick="foodObject('${cart.id}','${cart.name}','${cart.price}')">+</button></li>
           <li><button type="button" id = "dec" name="minus" onclick="deleteCart(${cart.id})">-</button></li> -->
        </ul>
          </div>
        `;
        cartlist.append(cartitem);
    }
    const cost = document.getElementById('last-option');
    cost.innerHTML = `
    <span>Total :${total}</span>
    `;
    cartlist.append(cost);
    renderHook.append(cartlist);
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
