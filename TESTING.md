# Testing documentation

* [Main README.mf file]()
* [Basty Shops]() live app
* [GitHub repository]()
***

## Table of contents

- [Manual testing documentation](#manual-testing)
- [Automated testing](#automated-testing)
- [User Testing](#user-testing)
***



| Reference | Test object | Expected result | Result 
| ----------- | ----------- | ----------- | ---------- |
| **HOME PAGE** |  |  | 
| 1 | Logo/Home links (header and footer) | Directs the user to home page | PASS
| 2 | Categories link | Directs the user to selected category page | PASS
| 3 | Logo/Home link | Directs the user to home page | PASS
| 4 | Burger menu button | Opens side menu | PASS
| 5 | Links buger menus | Directs the user to the selected page | PASS
| 6 | Search bar button | Shows the user the products in the category entered | PASS
| 7 | Profile link | Displays a dropdown menu | PASS
| 8 | Dropdows menu links in navbar | Directs the user to the action selected | PASS
| 9 | Buttons products carousel | Slide next content | PASS 
| 10 | Products link in products carousel | Directs user to the slected product detail page | PASS 
| 11 | Newsletter subscription | User receives real confirmation email | PASS  
| 12 | Footer links(all) | Direct the user to the selected page | PASS 
| 13 | Facebook link | Directs user to the Facebook Bussines page on a new window | PASS  
| **PRODUCTS PAGE** |  |  | 
| 14 | Categories badge | Directs user to the selected category products page | PASS
| 15 | Sort products by name(a-z) | Display products alphabetically cluttlered | PASS
| 16 | Sort products by price | Display products from the cheaper to the more expensive | PASS
| 17 | Products image link | Directs the user to the product detail page | PASS
| **PRODUCT DETAIL PAGE** |  |  | 
| 18 | Product multi images | Change product image on click | PASS
| 19 | Select product size | Get value of the selected size | PASS
| 20 | Out of stock | User can not select a size if out of stock | PASS
| 21 | Switch size buttons | Swith size button when clickin on a different one | FAIL
| 22 | Add product to wishlist | Add product to wishlist when clicking on the heart icon| FEATURE NOT AVAILABLE
| 23 | Product details | Display the respective product details and product description | PASS
| 24 | Add to bag button | Add product and size selected to shopping bag | PASS 
| 25 | Deals carousel | carousel buttons slide next corusel content | PASS
| 26 | Product images link | Images link in product caroulse direct the user to the selected product detail page | 
| 27 | Newsletter subscription | User receives real confirmation email | PASS 
| **BAG PAGE**|  |  | 
| 28 | Checkout buttons | Direct the user to the checkout page | PASS
| 29 | Increment quantity | + button increments product quantity by one | PASS
| 30 | Increment product price | + button increments product price by one | PASS
| 31 | Decrement quantity | - button decrements product quantity by one | PASS
| 32 | Decrement product price | - button decrements product price by one | PASS
| 33 | Remove product link | Removes the product from the shopping bag | PASS
| 34 | Grand total | Display the total of all the products together |
| 35 | EMpty bag | Displays empty bag message | PASS
| **CHECKOUT PAGE** |  |  | 
| 36 | Order summary | Diplays order summary correctly | PASS
| 37 | Checkout Form | Form only submits when all the required fields are filled | PASS
| 38 | Pre-populated fields | When a user is signed in and their shipping details have been saved on their profile, the corresponding fields are pre-populated | PASS
| 39 | Save details checkbox | When the delivery information checkbox is checked the user's profile is updated with the correct information after the form submission | PASS
| 40 | Log In and Sign Up Links (unsigned users) | The sign in and sign up links are displayed and redirected the user to the relevant page | PASS
| 41 | Card errors | Card errors message displays in case of: invalid card number, insufficient funds, etc. | PASS
| 42 | Card Charge notification | Is displayed to let the user know how much their card will be charged to verify that the figure matches the total in the order summary section |
| 43 | Complete Order button | Triggers the loading overlay before redirecting the user to the Checkout Success page |
| **CHECKOUT SUCCESS PAGE** |  |  | 
| 44 | Oreder Confirmation Email | If payment succeeds, the user receives a confirmation email with the order details | PASS
| 45 | Order Summary | Renders correctly with a list of the purchased products | PASS
| 46 | Order and Billing Info | Matches the information entered on the checkout form and displays correct totals | PASS
| 47 | Continue Shopping link | Redirects the user to the Products page |
| 48 | Stripe payment succeed webhook | If payment succeeds, Stripe shows webhook: payment_intent.succeeded with status 200 |
| ### CONTACT PAGE ### |  |  | 
| 49 | Form Validation | The form cannot be submitted without all the required fields being filled |
| 50 | Submit Button | Once clicked the form is cleared and a success message displays to inform the user that their message has been sent |
| **PROFILE PAGE** |  |  | 
| 51 | Personal details | Collapse displays user perosnal details | PASS
| 52 | Update details link | Directs the user to update details page and it renders a form | PASS
| 53 | Update details form | The form cannot be submitted without all the required fields being filled | PASS
| 54 | Update link | Redirects the user to Profile page and changes can be seen in Personal details Collapse | PASS
| 55 | Access | Collapse displays username and a link to change password | PASS
| 56 | Change password from Profile page | Link directs the user to Change password page and renders a form | PASS
| 57 | Change password form | The form cannot be submitted without all the required fields being filled | PASS
| 58 | Change password button | Password change success | PASS
| 59 | Order history | Collapse displays a list of the orders history | PASS
| 60 | Order number link | Directs user to the order details page | PASS
| 61 | Delivery information | Collapse displays a form to update the delivery information for next purchases | PASS
| 62 | Delivery information form | The form cannot be submitted without all the required fields being filled | PASS
| 63 | Saved delivery information | If the registered user saved their delivery information when making purchase, this will be diplayed in the form fields | PASS
| 64 | Update delivery information | Redirects the user to Profile page and changes can be seen in Delivery information link | PASS
| **ADD PRODUCT PAGE** |  |  | 
| 65 | Required Fields | Form does not submit unless required fields are correctly filled | PASS
| 66 | Dropdown Fields | All the categories and subcategories options appear in the dropdown fields | PASS
| 67 | Select Image LinK | Allows the user to upload an image from their device, and a message displays to the user the images' name | PASS
| 68 | Cancel Button | Redirects the user back to the products page | PASS
| 69 | Add Product Button | Redirects the user to the 'Product details' page for the new product with the correct information displayed | PASS
| **EDIT PRODUCT PAGE** |  |  |
| 70 | Form Fields	 | Form does not submit unless required fields are correctly filled | PASS
| 71 | Cancel Button | Redirects the user back to the 'Products' page | PASS
| 72 | Update Product Button | Updates any of the product information and redirects the user to the 'Product details' page for the edited product with the correct information displayed | PASS
| **BACK END CATEGORIES, PRODUCTS, SIZES** |  |  |
| 73 | Add new category | Superuser can add a new category | PASS
| 74 | Add new subcategory | Superuser can add a new subcategory | PASS
| 75 | Add new product | Superuser can add a new product | PASS
| 76 | Update product | Superuser can add update and existing product details | PASS
| 78 | Delete product | Superuser can delete a product | PASS
| 79 | Add new product sizes | Superuser can add new sizes to a product | PASS
| 80 | Update sizes stock | Superuser can update the stock of certain product sizes | PASS
| **SIGN IN** |  |  |
| 81 | Sign In Link | If the details are correct the user successfully logged in and redirected to the home page | PASS
| 82 | Forgot Password Link | Directs the user to the Password Reset page | PASS
| 83 | Sign Up Link | Directs the user to the sign up page | PASS
| **SINGN UP** |  |  |
| 84 | Sign Up Link |If the form is valid directs the user to the verify email address page and a confirmation email is sent to the user | PASS
| 85 | Sign In Link | Directs the user to the sign in page | PASS
| **SIGN OUT** |  |  |
| 86 | Sign Out button | Signs the user out of their account and redirects to the home page | PASS



 ### Automated testing


 ### Light house

 The site clearly needs some improvements in terms of accebility, performance and best practises

  - Desktop Home page

  ![Lighthouse desktop home page results](<media/Captura de pantalla (444).png>)

  - Mobile Home page
  
  ![Lighthouse mobile home page results](<media/Captura de pantalla (447).png>)

  - Products page desktop
  
  ![Lighthouse desktop products page results](<media/Captura de pantalla (449).png>)

- Products page mobile
  
  ![Lighthouse mobile products page results](<media/Captura de pantalla (451).png>)

  - Products detail page desktop
  
  ![Lighthouse desktop products page results](<media/Captura de pantalla (453).png>)

  - Products detail page mobile
  
  ![Lighthouse mobile products page results](<media/Captura de pantalla (455).png>)

### PEP8

  - All .py files went through PEP8 validator, only white spaces and long lines shown in test.


  - **Home page**


 ### Validators
 
  - [W3C CSS validator](https://jigsaw.w3.org/css-validator/)

      - No error reported
      ![CSS Results](<media/Captura de pantalla (429).png>)

  - [W3C HTML validator](https://validator.w3.org/nu/)
      
      - Showing lots of errors when using sintax {{ }} or {% blocks %}

      ![HTML validator results](<media/Captura de pantalla (437).png>)
      ![HTML validator results](<media/Captura de pantalla (438).png>)
      ![HTML validator results](<media/Captura_de_pantalla_270_2To9SKI.png>)

  - [JS Hint](https://jshint.com/)

       - JSHint was used to validate js files, only a few semicolons was missing and some variables unused.




