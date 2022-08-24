//jshint esversion:6

let countrySelected = $('#id_default_country').val();
if(!countrySelected){
    $('#id_default_country').css('color', 'rgb(111, 111, 111)');
}

$('#id_default_country').change(function(){
    countrySelected = $(this).val();
    if(!countrySelected){
        $('#id_default_country').css('color', 'rgb(111, 111, 111)');
    }else{
        $('#id_default_country').css('color', '#000');
    }
});
