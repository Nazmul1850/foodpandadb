var totalprice = 0;
var foodlist = [];


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
}

$(document).ready(function(){
  var memory = JSON.parse(sessionStorage.getItem("foodlist"));
  //console.log(memory);
  for(m in memory) {
    //console.log(memory[m].name);
    foodlist.push(new FoodCart(memory[m].id,memory[m].name,memory[m].price,memory[m].amount));
    totalprice += memory[m].price;
  }
});


$(document).ready(function(){
  const renderHook = document.getElementById('confirm-cart');
  const cartlist = document.getElementById('ol-confirm-cart');
  for (const cart of foodlist) {
      const cartitem = document.createElement('li');
      cartitem.classname = 'confirm-item';
      //console.log(cart.name);
      cartitem.innerHTML = `
      <div class="confirm-item-content">
          <span>${cart.name} (${cart.amount})</span>
          <span>/${cart.price}</span>
        </div>
      `;
      cartlist.append(cartitem);
  }
  const cost = document.getElementById('total-confirm');
  cost.innerHTML = `
      <span>Total :${totalprice}</span>
  `;
  cartlist.append(cost);
  renderHook.append(cartlist);

  $(".btn").click(function() {
    //alert("kkkkd");
    var foods = getString();
    var form = document.createElement("form");
    form.setAttribute("method", 'POST');
    form.setAttribute("action", '');
    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "foodids");
    hiddenField.setAttribute("value", foods);
    form.appendChild(hiddenField);

    csrfField = document.createElement("input");
    var csrftoken = getCookie('csrftoken');
    console.log("token" + csrftoken);
    csrfField.setAttribute("type", "hidden");
    csrfField.setAttribute("name", "csrfmiddlewaretoken");
    csrfField.setAttribute("value", csrftoken);
    form.appendChild(csrfField);
    document.body.appendChild(form);
    form.submit();
    sessionStorage.setItem("foodlist", "");
  });

});
function getString() {
  var foods = "";
  for (const cart of foodlist){
    foods += cart.id;
    foods += " ";
    foods += cart.amount;
    foods += " ";
  }
  return foods;
}

function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
