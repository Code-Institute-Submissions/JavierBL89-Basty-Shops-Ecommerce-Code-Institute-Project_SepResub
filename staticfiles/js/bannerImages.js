document.addEventListener("DOMContentLoaded", function(){

    window.omload = function(){
        bannerLoop();
    }
})

let bannerStatus = 1;
let bannerTimer = 4000;

function bannerLoop(){
    if (bannerStatus === 1){
        $('.hero-ban2').style.opacity = "0";
        setTimeout(function(){
            $('.hero-ban1').style.right = "0px";
            $('.hero-ban1').style.zIndex = "1000";

            $('.hero-ban2').style.right = "-1200px";
            $('.hero-ban2').style.zIndex = "1500";

            $('.hero-ban3').style.right = "1200px";
            $('.hero-ban3').style.zIndex = "500";
        }, 500);
        setTimeout(function(){
            $('.hero-ban2').style.opacity = "1";
            bannerStatus = 1
        }, 1000);

    }else if (bannerStatus === 2){
            $('.hero-ban3').style.opacity = "0";
            setTimeout(function(){
                $('.hero-ban2').style.right = "0px";
                $('.hero-ban2').style.zIndex = "1000";

                $('.hero-ban3').style.right = "-1200px";
                $('.hero-ban3').style.zIndex = "1500";

                $('.hero-ban1').style.right = "1200px";
                $('.hero-ban1').style.zIndex = "500";
            }, 500);
            setTimeout(function(){
                $('.hero-ban3').style.opacity = "1";
                bannerStatus = 3;
            }, 1000);

    }else if (bannerStatus === 3){
        $('.hero-ban1').style.opacity = "0";
        setTimeout(function(){
            $('.hero-ban3').style.right = "0px";
            $('.hero-ban3').style.zIndex = "1000";

            $('.hero-ban1').style.right = "-1200px";
            $('.hero-ban1').style.zIndex = "1500";

            $('.hero-ban2').style.right = "1200px";
            $('.hero-ban2').style.zIndex = "500";
        }, 500);
        setTimeout(function(){
            $('.hero-ban1').style.opacity = "1";
            bannerStatus = 1;
        }, 1000);

}

}