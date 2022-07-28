// Handle product purchase form

const form = $('#purchase-form');
const options = $('.size-box');
const redirect_url = $("#redirect_url").val();
let item_id = $("#item_id").val();

console.log(`URL: ${redirect_url}`);

for (choice of options){
    // console.log(puta);
    var size
    choice.addEventListener('click', function(){
        var sizevalue = $(this).val()
        $(this).addClass("active")
        size = parseInt(sizevalue)
    });
};


form.on('submit', function(ev){
    ev.preventDefault();

    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'item_id': item_id,
        'size': size,
        'redirect_url': redirect_url,
    };
    var url = `/add/${item_id}`;

    $.post(url, postData).done(function (){
    }).then(function(result) {
        if (result.error) {
            console.log(error);
        }else{
            form.submit();
        }
        })
});