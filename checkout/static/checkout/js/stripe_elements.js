var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
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

