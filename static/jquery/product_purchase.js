// Handle product purchase form

const form = $('#purchase-form');
const options = $('.size-box');
const redirect_url = $("#redirect_url").val();
let item_id = $("#item_id").val();
console.log(`URL: ${redirect_url}`);

for (choice of options){
    choice.addEventListener('click', function(){
        $(this).attr('id', 'active');
        $(this).css('background-color', 'rgb(122, 13, 13)');
        $(this).css('color', 'white');

    });
};

form.on('submit', function(ev){
    ev.preventDefault();
    // Get product size
    let size = $('#active');
    size = parseInt(size.attr('value'));
    // Get product size id
    let size_id = $('#active');
    
    for(i of size_id){
           if(i){
                let size_id_first_number = size_id.attr('value')[3];
                let size_id_second_number = size_id.attr('value')[4];
                size_id = parseInt(size_id_first_number + size_id_second_number)
            
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
           }
    }

});