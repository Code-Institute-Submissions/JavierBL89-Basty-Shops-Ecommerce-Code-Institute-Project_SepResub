//jshint esversion:6

const form = $('#contact-form');

form.on('submit', function(ev) {
    ev.preventDefault();
    sendEmail();
});

function sendEmail(){
    const name = $('#name').val();
    const email = $('#email').val();
    const message = $('#message').val();
    const puta = document.getElementById('contact-container');
    const successMessage = `
                <div class="col" id="message-box">
                <h6 class="message fw-bold">Thanks for taking your time, keep an eye on your inbox!</h6>
                <div class="row text-center mt-5">
                <a class="back-home" href="/"> BACK HOME</a>
                </div>
                </div>
                `;
    const failedMessage = `
                    <div class="col" id="message-box">
                    <h6 class="message fw-bold">Ups! Something went wrong. Try again at another time!</h6>
                    <div class="row text-center mt-5">
                    <a class="back-home" href="/"> BACK HOME</a>
                    </div>
                    </div>
                    `;
    emailjs.send("service_0vu276l", "customer support", {
        "from_name" : name,
        "from_email": email,
        "message": message
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            setTimeout(function(){
                puta.innerHTML = successMessage;

            },0.700);
        },
        function(error) {
            console.log("FAILED", error);
            setTimeout(function(){
                puta.innerHTML = failedMessage;
            },0.700)
        }
    );
};