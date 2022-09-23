//jshint esversion:6

// Handle product purchase form

const form = $('#purchase-form');
const options = $('.size-box');
const redirect_url = $("#redirect_url").val();
let item_id = $("#item_id").val();
console.log(`URL: ${redirect_url}`);

for (let choice of options){

    choice.addEventListener('click', function(){
      options.css('background-color', 'white');
      let sizeChoise = $(this).text();
      let element = $(this);
      changeBackground(sizeChoise, element);
      $(this).attr('id', 'active');
      $(this).attr('class', 'size-box text-center py-1 active');
      // Get product input value size
      let size = $('#active');
      size = size.attr('value');
    });
}

/***
* FUNCTION TO SWICTH PRODUCT SIZE BACKGROUND COLOR WHEN CLICKING
*/
function changeBackground(sizeChoise, element){

  if(sizeChoise == '36'){
    element.css('background-color', 'rgb(122, 13, 13)');
   }
  else if(sizeChoise == '37'){
    element.css('background-color', 'rgb(122, 13, 13)');
  }
  else if(sizeChoise == '38'){
    element.css('background-color', 'rgb(122, 13, 13)');
  }
  else if(sizeChoise == '39'){
    element.css('background-color', 'rgb(122, 13, 13)');
  }
  else if(sizeChoise == '40'){
    element.css('background-color', 'rgb(122, 13, 13)');
  }
  else{
    element.css('background-color', 'white');
  }
}


form.on('submit', function(ev){
    ev.preventDefault();
    // Get product input value size
    let size = $('#active');
    size = parseInt(size.attr('data-value'));
    // Get product size id
    let size_id = $('#active');
    
    let size_id_first_number = size_id.attr('data-value')[3];
    let size_id_second_number = size_id.attr('data-value')[4];
    size_id = parseInt(size_id_first_number + size_id_second_number);

    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'item_id': item_id,
        'product_size': size,
        'size_id': size_id,
        'redirect_url': redirect_url,
    };
    var url = `/bag/add/${item_id}/`;
    
    $.post(url, postData).done(function (){
    }).then(function(result) {
        if (result.error) {
            console.log(error);
        }else{
            location.reload();
        }
        });

});