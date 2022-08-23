# BASTY SHOPS

This is ecommerce store that sells shoes for women.
Allows users to check out products clasiffied into categories, select a specific size of the product and securily checkout through Stripe payment platform.

Users can create their account, and subscribe to the store's newsletter.
Users can make an order without being registered.
Users can easily update their personal information and delivery information.
The site provides all the information needed about delivery, returns and refounds as well as a FAQs section to solve common questions.

Users can easily contact customer support.

- Live store [Basty Shops](<https://bastyshops.herokuapp.com>)

## Table of contents

### [Planning stage](#planning-stage)

- Target audience
- User Stories
- Design goals
- Design choises
- Font
- Color squeme
- Wireframes
- Flow chart
- Web Strategy

### [Features](#features)

- SingUp
- Social Authentication
- Update profile information
- Update site's access information
- Orders history
- Update user's delivery address
- Search products by name or category
- Sort products by price, rating or alphabetically
- Show total in the bag
- Modify product quantity on the bag page
- Checkout
- Payment
- Confirmation email
- Contact customer support by email
- Activity info messages

### [Testing](#testing)

- Manual testing
- Light house
- Validators

### [Technology Used](#technology-used)

- Lnguages
- Libraries
- Frameworks

### [Bugs](#bugs)

- Fixed bugs
- Unfixed bugs

### [Deployment](#deployment)


### [Credits](#credits)

- Content
- Acknowledgements
- Aditiona information

## Planning stage

### Target audience

The site goals is to buy as many products as posible whether if it is for personal use or for making a present.
The site is potentianly designed to lure in women from 16 to 40 years old who are looking to buy a new pair of shoes or they potentially will buy it in future.
Anyone over 16 can maake a purchase.
The site offers a wide range of different type of shoes in order to widen potential customers at any time along the year. 

### User stories

- Can follow Iteration boards [here](https://github.com/JavierBL89/Basty-Shops-Ecommerce-Code-Institute-Project/projects?query=is%3Aclosed&type=classic#credits)

![User stories](<media/Captura de pantalla (364).png>)
![User stories](<media/Captura de pantalla (363).png>)
![User stories](<media/Captura de pantalla (365).png>)


### Design goals

- Minimalistic design
- Well structured information
- Easy readability
- Intuitive straightforward navigation
- Straightfroward forms
- Resposive for all screen sizes

  - ###### Desktop

  ![Desktop design](<media/Captura de pantalla (369).png>)

  - ###### Tablet
  
  ![Tablet design](<media/Captura de pantalla (370).png>)

  - ###### Mobile

  ![Mobile design](<media/Captura de pantalla (371).png>)


### Design choises

#### Fonts 

- Roboto san-serif

#### Color scheme

- Body background color: #ffff;
- Main theme red color: rgb(122, 13, 13);
- Backgroun buttons and anchor color: #FF6542;
- Subscription container background; #C8BFC7;
- Other yellow texts: #F3FFC6;

### Wireframes

- For wireframing i used [Balsamiq wireframe](https://balsamiq.com/wireframes/) which is not a free tool anymore.

- #### Home page Desktop wireframe

![Home page wireframe](<media/desktop-wireframe (2).png>)

- ###### Home page Mobile wireframe

![Desktop wireframe](<media/mobile-wireframe.png>)

- #### Products page Desktop & Mobile wireframe

![Desktop & Mobile products page wireframe](<media/products-page-wireframe.png>)


- #### Product detail page Desktop & Mobile wireframe

![Desktop & Mobile product detail page wireframe](<media/products-detail-page-wireframe.png>)


### Flowchart

- For this i used an online app [Lucidchart](https://www.lucidchart.com/) which is not a free app.

- #### Database structure

![Basty Shops Db structure](<media/db-structure.png>)

### Marketing Stragtegy

* Potential customers

  - Women from 16 to 40 years old

* Potential platforms:

  - Instagram
  - Facebook
  - Youtube

* Potential customers might need:

  - Boots
  - Sneakers
  - Shoes
  - Free shipping
  - Easy exchange
  - customer support
  - Live support
  - Reviews
  - Images
  - Deals
  - Discounts

* Web Marketing will run sales, and offer deals and discounts and will use images and keywords to make an emotial response in order to potential customers to click and visit the store

* Potential customers might want to hear about this offers through SMM (Social Media Marketing)

* The company will have a 3000€ budget for SMM during the very first year

* Marketing will be focused on SMM, both organic and Paid along with Email Marketing

  - Google adds will be disscused late in year

* SEO:

  - Keaywords research will help to build a valuable content for Google ranking, and to draw attention to potential customers.

  - Keywords research stats at the time:

| Keyword | V | Comp |
| ----------- | ----------- | ----------- |
| boots | 480 | 60,77 | 
| heels | 264 | 47,21 |
| sneakers | 563,33 | 48,66 |
| heeled boots | 41,775 | 15,06 |
| platform boots | 141,500 | 15,08 |
| sandals for women | 205,375 | 15,95 |
| sneakers for women | 149,042 | 14,35 |
| women's shoes | 489,500 | 23,8 |
| women's boots | 407,125 | 14,96 |
| wedding shoes low heel | 13,708 | 6,81 |
| chunky boots | 117,25 | 19 |
| boots for women | 407,125 | 21,59 |

* [Facebook Store page](https://www.facebook.com/Basty-Shops-102175379293385)

![Facebook store image](<media/Captura de pantalla (418).png>)

## Features

- SingUp

  - Users can register in the site by filling up a form

![SingUp form](<media/Captura de pantalla (372).png>)

- Social Authentication
 
  - Users can singup using their social accounts in order to speed up and ease site's registration or login,
  as well as to improve their security 

  ![SingUp form](<media/Captura de pantalla (372).png>)


- Update profile information

  - Registered users can easily **update their personal information** or delete their account

  ![Update peronal info](<staticfiles/flags/Captura de pantalla (375).png>)

  - Registered users can easily **update their access informatio**n clicking on the link

  ![Update access info](<media/Captura de pantalla (377).png>)

  - Registered users can easily **check their order's history**

  ![Check order's history](<media/Captura de pantalla (379).png>)

  - Registered users can easily **update their delivery address**

  ![Update delivery address](<media/Captura de pantalla (383).png>)

- Search products by name or category

  - Users can easily search products by entering name or key words

    ![Products searcher](<media/Captura de pantalla (385).png>)

- Sort products by price or alphabet

  - Users can easily sort products by entering their preference (by rating will be implemented in future)

    ![Products sorter](<media/Captura de pantalla (387).png>)

- Show total in the bag

  - Users can see the total of their shopping bag on the bag page

    ![Total shopping bag](<media/Captura de pantalla (389).png>)

- Modify product quantity on the bag page

  - Users can modify the total of a specific item from their shopping bag

    ![Modify product quantity](<media/Captura de pantalla (393).png>)

- Checkout

  - Users can make their order by **filling up the checkout page**
  - Users can see their **order summary**
  - Registered users can save the **delivery information** for future purchases

    ![Checkout](<media/Captura de pantalla (395).png>)

- Payment

  - Users can securely **make a payment** using theit credir, debit, or american express or any other type of card throught a well trusted payment platform [Stripe](<https://stripe.com/en-ie>)

    ![Checkout](<media/Captura de pantalla (395).png>)

- Confirmation email

  - Users will receive a **confirmation email** after making a successful purchase

    ![Checkout](<media/Captura de pantalla (395).png>) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

  - Contact customer support y email

  - Users can **send an email to customer support** by going into "Contact us" page

    ![Contact customer support](<media/Captura de pantalla (403).png>)

  - User's activity messages

  - Users will be informed after every acction on the site thrught automatic messages 

    ![Activity messages](<media/Captura de pantalla (405).png>)

## Future features

 - Add products to wish list
 - Add reviews and rating to products if needed
 - Add customers testimonials
 - Paypal payments
 - Google payments
 
 Note: Reviews is alredy added into database structure. Wish list is not, however it is implemented in html files with not functionality(due to lack of time).

 ## Testing

 ### Manual Testing


 ### Automated testing


 ### Light house


 ### Validators


 ## Technology Used

 * ### Languages
  
    - Languages used according to [Github](https://github.com/) reports.

  ![Languages used](<media/Captura de pantalla (420).png>)

 * ### Libraries
    
    - [Boostrap](https://getbootstrap.com/)
    - [JQuery](https://jquery.com/)
    - [Fontawsome](https://fontawesome.com/)
    - [Google fonts](https://fonts.google.com/)

* ### Frameworks

    - [Django](https://www.djangoproject.com/)
    - All packages installed can be found in [requirements.txt](https://github.com/JavierBL89/Basty-Shops-Ecommerce-Code-Institute-Project/blob/main/requirements.txt)

## Bugs

  * Unfixed bug
    
      - On the bag page, for every item added the layout changes by adding rows in a scalate way
      Every new row to be pushed to the left.

      ![Items bag page](<media/Captura de pantalla (422).png>)

  * Unfixed bug
    
      - On the bag page, after adding the first item into the shopping bag, the following items seem to not have the disabel buttons functionality applied. This issue must be related the previous one 
      
      ![Products quantity input](<media/Captura de pantalla (424).png>)

   <!-- * Unfixed bug
    
      - Adding a block extra_css tag to every page for the differents apps in order to link them to their own css folder in the app seems to not work for me. After adding this tag and link them to their css file, the styling kept being applied from the stylesheet link added into the base template -->

 * Unfixed bug
    
      - When adding products into shopping bag, the toast showing a success message does not show, however it does when removin items from the shopping bag.
      The code to me looks fine, it prints the print statements i set, also i do not get any error and the the code when running goes through the next function and everything works fine...

      ![Code snippet](<media/Captura de pantalla (426).png>)

 ### Fixed bugs

  * Fixed bug
    
      - Error "TypeError:'dic_values' object is not supscritable
      This occurs when trying to access dic_values object at a specific index(slicing)
      
      I go this error when trying to acces to images list of every product
      
      * Fix: Convert the dict into a list  `list(my_dict.values())[2:]`

  * Fixed bug:

      - The increment and decrement buttons on the bag page gave me a really hard time.
      The buttons would never triggered the js code. I used as in the walk through project the file
      'quantity_form_scripts.html' placed into 'products/includes' folder.

      * Fix: I fix this by getting rid of the above file and placeing the js script in the 'quantity_form.html' file down the file inside the postblockjs tag, then then buttons worked!!

  * Fixed bug:

      - When deploying into heroku could not build a wheel for backports.zoneinfo
      It seems that Heroku by default uses Python vrsion 3.10.x and backports.zoneinfo no works properly with that version of Python 

      * Fix: Create a runtime.txt in the root directory and write your Python version,
       in my case python-3.8.11. Commit and push changes.


## Deployment

The project was deployed to Heroku using the below procedure:-

- Log in to Heroku or create an account if required.
- Click the button labeled New from the dashboard in the top right corner, just below the header.
- From the drop-down menu select "Create new app".
- Enter a unique app name.
- Once the web portal shows the green tick to confirm the name is original select the relevant region. In my case, I chose Europe as I am in Ireland.

- When happy with your choice of name and that the correct region is selected, click on the "Create app" button.
- Go to tap "Resources" and add a new add-on "Heroku Postgres"
- Copy the database url.
- This will bring you to the project "Deploy" tab. From here, navigate to the settings tab and scroll down to the "Config Vars" section.
- And paste it in value field of "Reveal Config Vars"
- Click the button labelled "Reveal Config Vars" and enter the "keys" and  "values"you need, and click the "add" button.
- Scroll down to the buildpacks section of the settings page and click the button labeled " add buildpack," select "Python," and click "Save Changes".
- Scroll back to the top of the settings page, and navigate to the "Deploy" tab.
- From the deploy tab select Github as the deployment method.
- Confirm you want to connect to GitHub.
- Search for the repository name and click the connect button next to the intended repository.
- From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:
- Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.
- Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.


<!-- * If using [AWS](https://s3.console.aws.amazon.com) services to store static and media files -->

## Credits

 ### Code

 For the porpouse of developing this proyect i had to look into some youtube tutorials and web sites.

  * #### Databases relationships
   
  -[Entity Database Relationships](<https://www.youtube.com/watch?v=QpdhBUYk7Kk&list=PLHtuMzYFHMqz4h2gnFL44VZRt0s0HGxN4&index=1>)
  

  * #### Social Authentication

  -[Social Authentication](<https://www.youtube.com/watch?v=-TUEM2NCuVE&list=PLHtuMzYFHMqwVa6AglqPNMShrkySsfPTY&index=7&t=308s>)

  * #### Stripe

  - All the code to implement **Stripe** is taken from the walk through Boutiue Ado with [Code Institute](https://codeinstitute.net/ie/), i never copied and paste away, i wrote everyting by following my notes or the video lessons when needed.

  ### Media

  - Products pictures were taken from different stores, which is why they are differrent sizes and changes the layout in certain card products.

  - Home page images were taken from [Google images](<https://images.google.com/>)

# Aknowlegments

I want to thank the [Code Institute](https://codeinstitute.net/ie/) tutor assistance team, which helped me out with some of the day to day code issues. I could have never complete this project without them!

I did not make use of my mentor assistance this time round. 


