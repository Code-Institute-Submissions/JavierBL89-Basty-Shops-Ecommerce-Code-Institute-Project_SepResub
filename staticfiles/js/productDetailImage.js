/* Ddocument onload */


jQuery(function(){
    
    list = $(".product-image");
    list.on("click", function(){
        newImage = this.getAttribute("src")
        mainImage = $("img")[0].setAttribute("src", newImage)
        console.log(mainImage);
    });
    
});