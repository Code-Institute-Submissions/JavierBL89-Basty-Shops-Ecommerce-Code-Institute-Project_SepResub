var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();


const appearance = {
    theme: 'stripe',
  
    variables: {
      color: '#000',
      colorDanger: '#df1b41',
      fontFamily: 'Helvetica Neue, Helvetica, sans-serif',
      '::placeholder': {
        color: "#aab7c4"
      },
      invalid: {
        color: '#mdc3545',
        incolor: '#dc3545'
      }
    }
  };
  
var card = elements.create('card', {'appearance': appearance});
card.mount('#card_element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
      var html = `
          <span class="icon" role="alert">
              <i class="fas fa-times"></i>
          </span>
          <span>${event.error.message}</span>
      `;
      $(errorDiv).html(html);
  } else {
      errorDiv.textContent = '';
  }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    // Desable card element and submit button to prevent multiple submissions
    card.update({'disable': true});
    $('#submit-button').attr('disabled', true)
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
    payment_method: {
    card: card,
    }
    }).then(function(result) {
         if (result.error) {
             var errorDiv = document.getElementById('card-errors');
             var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
             $(errorDiv).html(html);
             $('#payment-form').fadeToggle(100);
             $('#loading-overlay').fadeToggle(100);
             // re-enable card element and submit button if error to allow users to fix it
             card.update({'disable': false});
             $('#submit-button').attr('disabled', false)
         } else {
             if (result.paymentIntent.status === 'succeeded') {
                 form.submit();
          }
        }
     });
});