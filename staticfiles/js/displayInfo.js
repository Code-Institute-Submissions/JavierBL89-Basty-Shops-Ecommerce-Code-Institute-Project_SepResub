
const profileInfo = $('.profile-info');

for(row of profileInfo){

    row.addEventListener('click', function(){

        if(this.getAttribute("id") === "personal-details"){
            $(".profile-details-content").toggle();
        }
        else if(this.getAttribute("id") === "access"){
            $(".access-profile-content").toggle();

        }
        else if(this.getAttribute("id") === "delivery-info"){
            $(".delivery-info-content").toggle("slow");
        }
        else if(this.getAttribute("id") === "order-history"){
            $(".order-history-content").toggle("slow");
        }
    });
}