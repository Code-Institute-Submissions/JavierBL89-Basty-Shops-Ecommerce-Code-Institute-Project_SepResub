// Handle product purchase form

const form = $('#purchase-form');
const options = $('.size-box');
const redirect_url = $("#redirect_url").val();
let item_id = $("#item_id").val();

console.log(`URL: ${redirect_url}`);

for (choice of options){
    // console.log(puta);
    size = choice.addEventListener('click', function(){
        var sizevalue = $(this).val()
        $(this).addClass("active")
        size = parseInt(sizevalue)
        console.log(size);
    });
};


for (active of options){
    // console.log(puta);
    if(active.getAttribute('class') == 'active'){
        size = this.val()
    }
};

form.on('submit', function(ev){
    ev.preventDefault();

    var size = parseInt($('active').val());
    
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'item_id': item_id,
        'size': size,
        'redirect_url': redirect_url,
    };
    var url = `/add/${item_id}`;
    alert(size)
    $.post(url, postData).done(function (){
    }).then(function(result) {
        if (result.error) {
            console.log(error);
        }else{
            console.log(size);

            form.submit();
        }
        })
});