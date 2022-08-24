//jshint esversion:6

/* Ddocument onload */


jQuery(function(){

    let list = $(".product-image");
    list.on("click", function(){
       let newImage = this.getAttribute("src")
       let mainImage = $("img")[0].setAttribute("src", newImage)
        console.log(mainImage);
    });
    
});