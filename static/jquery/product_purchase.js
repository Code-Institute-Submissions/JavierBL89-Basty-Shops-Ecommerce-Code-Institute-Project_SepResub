// Handle product purchase form

const form = $('#purchase-form');
const options = $('.size-box');
const redirect_url = $("#redirect_url").val();
let item_id = $("#item_id").val();

console.log(`URL: ${redirect_url}`);

for (choice of options){
    choice.addEventListener('click', function(){
        $(this).attr('id', 'active');
    });
};


form.on('submit', function(ev){
    ev.preventDefault();

    var size = parseInt($('#active').val());
    console.log(size)

    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'item_id': item_id,
        'product_size': size,
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
        })
});