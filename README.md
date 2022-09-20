# BASTY SHOPS

![Basty Shops screen size desing](<media/site-screen-sizes.png>)

This is a B2C ecommerce store for the final project of the Code Institute diploma in Software Development.

The appication is focused on selling products to users, especifically shoes for women.

It allows users to check out products clasified into categories, select a specific product and size, add it to the shopping bag and securily checkout through Stripe payment platform.
This app does not take real payments.
In order to complete a purchase to test it out, you must enter on the credit card field the following details:

* Card number:  4242 4242 4242 4242
* Any future expiry date, such as 04/24.
* Any three-digit CVC.
* Same Post code as in delivery form

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, newsletter subcription, and full CRUD functionality for approved users for Products.
Users can easily update their personal information and delivery information.
The site provides all the information needed about delivery, returns and refounds as well as a FAQs section to solve common questions.
Users can contact customer support.

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
- Management
  - Add product
  - Edit product
  - Delete product

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
### [Making a Local Clone](#making-a-local-clone)
### [Forking repository](#forking-repository)
### [Setting up your local enviroment](#setting-up-your-local-enviroment)
### [Getting Stripe keys](#getting-stripe-keys)
### [Getting email variables from gmail](#getting-email-variables-from-gmail)
### [Setting AWS bucket](#setting-aws-bucket)




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

![User stories](<media/Captura de pantalla (554).png>)
![User stories](<media/Captura de pantalla (556).png>)
![User stories](<media/Captura de pantalla (558).png>)


### Design goals

- Minimalistic design
- Well structured information
- Easy readability
- Intuitive straightforward navigation
- Straightfroward forms
- Resposive for all screen sizes

  - ###### Desktop

  ![Desktop design](<media/Captura de pantalla (562).png>)

  - ###### Tablet
  
  ![Tablet design](<media/Captura de pantalla (563).png>)

  - ###### Mobile

  ![Mobile design](<media/Captura de pantalla (564).png>)

[Back to top](#table-of-contents)

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

![Basty Shops Db structure](<media/Captura de pantalla (292).png>)

[Back to top](#table-of-contents)

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

![Facebook store image](<media/Captura de pantalla (566).png>)

## Features

- ### SingUp

  - Users can register in the site by filling up a form

![SingUp form](<media/Captura de pantalla (578).png>)

- ### Social Authentication
 
  - Users can singup using their social accounts in order to speed up and ease site's registration or login,
  as well as to improve their security 

  ![SingUp form](<media/Captura de pantalla (578).png>)


- ### Update profile information

  - Registered users can easily **update their personal information** or delete their account

  ![Update peronal info](<media/Captura de pantalla (579).png>)

  - Registered users can easily **update their access information** clicking on the link

  ![Update access info](<media/Captura de pantalla (591).png.png>)

  - Registered users can easily **check their order's history**

  ![Check order's history](<media/Captura de pantalla (581).png>)

  - Registered users can easily **update their delivery address**

  ![Update delivery address](<media/Captura de pantalla (582).png>)

- ### Search products by name or category

  - Users can easily search products by entering name or key words

    ![Products searcher](<media/Captura de pantalla (583).png>)

- ### Sort products by price or alphabet

  - Users can easily sort products by entering their preference (by rating will be implemented in future)

    ![Products sorter](<media/Captura de pantalla (584).png>)

- ### Show total in the bag

  - Users can see the total of their shopping bag on the bag page

    ![Total shopping bag](<media/Captura de pantalla (585).png>)

- ### Modify product quantity on the bag page

  - Users can modify the total of a specific item from their shopping bag

    ![Modify product quantity](<media/Captura de pantalla (586).png>)

- ### Checkout

  - Users can make their order by **filling up the checkout page**
  - Users can see their **order summary**
  - Registered users can save the **delivery information** for future purchases

    ![Checkout](<media/Captura de pantalla (587)-2.png>)

- ### Payment

  - Users can securely **make a payment** using theit credir, debit, or american express or any other type of card throught a well trusted payment platform [Stripe](<https://stripe.com/en-ie>)

    ![Checkout](<media/Captura de pantalla (588)-2.png>)

- ### Confirmation email

  - Users will receive a **confirmation email** after making a successful purchase

    ![Checkout](<media/Captura de pantalla (589)-2.png>)

- ### Contact customer support y email

  - Users can **send an email to customer support** by going into "Contact us" page

    ![Contact customer support](<media/Captura de pantalla (593).png>)

  - User's activity messages

  - Users will be informed after every acction on the site thrught automatic messages 

    ![Activity messages](<media/Captura de pantalla (602).png>)

- ### Management

  - Add product

  Store admin will be able to add products from the site so much easily the from the Django admin panel
  
    ![Add product admin](<media/Captura de pantalla (597).png>)

  - Edit product

  Store admin will be able to edit products from the site so much easily the from the Django admin panel
  
    ![Edit product admin](<media/Captura de pantalla (598).png>)

  - Delete product

  Store admin will be able to delete products easily from the site
  
    ![Delete product admin](<media/Captura de pantalla (599).png>)


[Back to top](#table-of contents)

## Future features

 - Add products to wish list
 - Add reviews and rating to products if needed
 - Add customers testimonials
 - Paypal payments
 - Google payments
 
 Note: Reviews is alredy added into database structure. Wish list is not, however it is implemented in html files with not functionality(due to lack of time).


 ## Technology Used

 * ### Languages
  
    - Languages used according to [Github](https://github.com/) reports.

  ![Languages used](<media/Captura de pantalla (604).png>)

 * ### Libraries
    
    - [Boostrap](https://getbootstrap.com/)
    - [JQuery](https://jquery.com/)
    - [Fontawsome](https://fontawesome.com/)
    - [Google fonts](https://fonts.google.com/)

* ### Frameworks

    - [Django](https://www.djangoproject.com/)
    - All packages installed can be found in [requirements.txt](https://github.com/JavierBL89/Basty-Shops-Ecommerce-Code-Institute-Project/blob/main/requirements.txt)

[Back to top](#table-of-contents)


## Bugs

 * Unfixed bug
    
      - When adding products into shopping bag, the toast showing a success message does not show, however it does when removing items from the shopping bag.
      The code to me looks fine, it prints the print statements i set, also i do not get any error and the the code when running goes through the next function and everything works fine...

      ![Code snippet](<media/Captura de pantalla (426).png>)

  * Unfixed bug
    
      - In large screens css starts to overflow.

      ![Code snippet](<media/Captura de pantalla (606).png>)


 ### Fixed bugs

  * Fixed bug
    
      - Error "TypeError:'dic_values' object is not supscritable
      This occurs when trying to access dic_values object at a specific index(slicing).
      
      I go this error when trying to acces to images list of every product.
      
      * Fix: Convert the dict into a list  `list(my_dict.values())[2:]`


  * Fixed bug:

      - When deploying into heroku could not build a wheel for backports.zoneinfo
      It seems that Heroku by default uses Python vrsion 3.10.x and backports.zoneinfo no works properly with that version of Python 

      * Fix: Create a runtime.txt in the root directory and write your Python version,
       in my case python-3.8.11. Commit and push changes.

  * Fixed bug
    
      - On the bag page, for every item added the layout changes by adding rows in a scalate way.
      Every new row to was pushed to the left.

      ![Items bag page](<media/Captura de pantalla (422).png>)

      - The problem was having the form closing tag in the wrong line


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

## Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JavierBL89/Basty-Shops-Ecommerce-Code-Institute-Project.git)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/JavierBL89/Basty-Shops-Ecommerce-Code-Institute-Project.git
```

7. Press Enter. Your local clone will be created.

## Forking Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JavierBL89/Basty-Shops-Ecommerce-Code-Institute-Project.git)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

## Setting up your local enviroment

1. Create and run a Python virtual environment in your computer's terminal .

    `python3 -m venv env`

    `. env/bin/activate`

 Or use gitpod built in virtual enviroment feature.

2. Create env.py file. It needs to contain those 5 variables.

* Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app. 
* Secret_key - is the django secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
* Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 
* Google API key can be obtained [here](https://cloud.google.com/gcp?authuser=1) you will have to register with google and create new app to get the API key. Follow the instructions on the website.

```
DEVELOPMENT
SECRET_KEY

STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY 
STRIPE_WH_SECRET

```
PostgreSQL and AWS keys are needed only on Heroku, not in local IDE

3. Run command 
```
pip3 install -r requirements.txt
```

## Getting Stripe keys

Go to developers tab. On side menu you will find API keys. Copy STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY.

Go to Webhooks. Click Add Endpoint button in top right hand corner.
Add endpoint URL (your local or deployed URL)
Add all events 
Than click add endpoint
You should be redirected to this webhook's page. Reveal webhook sign in secret and copy to Settings and to heroku as STRIPE_WH_SECRET variable

## Getting email variables from gmail

- Log into gmail account
- Go to Settings and than See all settings
- Top menu go to Accounts and import
- Find on the list Other google account settings
- Left side menu - Security
- Turn on two step verification: add phone number and follow instructions
- Go back to security
App passwords - Select Mail, Select Device - Other, Django, Copy app password.

In Heroku 
EMAIL_HOST_PASS is the password copied from above.
EMAIL_HOST_USER is the gmail email address

## Setting AWS bucket

1. Go to [Amzon Web Services](https://aws.amazon.com/) page and login or register

2. You should be redirected to AWS Managment Console, if not click onto AWS logo in top left corner or click Services icon and choose Console Home

3. Below the header AWS Services click into All Services and find **S3** under Storage

4. Create New Bucket using **Create Bucket** button in top right hand corner

- **Configuration:** type in your chosen name for the bucket (preferably matching your heroku app name) and AWS Region closest to you

- **Object ownership:** ACLs enabled, Bucket owner prefered

- **Block Public Access settings:** Uncheck to allow public access, Acknowledge that the current settings will result that the objects within the bucket will become public

- Click **Create Bucket**

5. You are redirected to Amazon S3 with list of your buckets. Click into the name of the bucket you just created

6. Find the tab **Properties** on the top of the page:
**Static website hosting** at the bottom of the properties page: clik to edit, click enable, fill in index document: index.html and error.html for error

7. On the **Permissions** tab:
- Cross-origin resource sharing (**CORS**) Paste in the below code as configuration and save

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- **Bucket Policy** within permissions tab: Edit bucket policy
Click AWS Policy Generator (top right corner)

Select type of policy: S3 Bucket policy
Principal: * (allows all)
Actions: Get object
Amazon Resource Name (ARN): paste from the Edit bucket policy page in permissions
Click Add statement Than Click Generate Policy and Copy the policy into bucket policy editor. 
In the policy code find "Resource" key and add "/*" after the name of the bucket to enable all
Save changes

- **Access control list (ACL)** within permissions tab: click Edit

find Everyone (public access) and check List box and save

8. Identity and Access Management (IAM)
Go back to the AWS Management Console and find IAM in AWS Services

- side menu - User Groups and click **Create Group**
name group "manage-your-app-name" and click Create group

- side menu - Policies and click **Create Policy**
Click import managed policy - find AmazonS3FullAccess
Copy ARN again and paste into "Resource" add list containint two elements "[ "arn::..", ""arn::../*]" First element is for bucket itself, second element is for all files and foldrs in the bucket

Click bottom right Add Tags, than Click bottom right Next: Review
Add name of the policy and description

Click bottom right Create policy

9. Attach policy to the group we created:
- go to User Groups on side menu
- select your group from the list
- go to permissions tab and add permissions drop down and choose **Attach policies**
- find the policy created above and click button in bottom right Add permissions

10. Create User to go in the group
- **Users** in the side menu and click add users

User name: your-app-staticfiles-user
Check option: Access key - Programmatic access
Click button at the bottom right for Next
- Add user group and add user to the group you created earlier
Click Next Tags and Next: review and Create user
- Download .csv file


11. Connect django to AWS S3 bucket
- install boto3
- install django-storages
- freeze to requirements.txt
- add storages to installed apps in settings.py

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

12. Go to heroku to set up enviromental variables

open CSV file downloaded earlier and copy each variable into heroku Settings

AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID from csv
AWS_SECRET_ACCESS_KEY from csv
USE_AWS = True
remove DISABLE_COLLECTSTATIC variable from heroku

13. Create file in root directory custom_storages.py

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

14. Go to settings.py, add the AWS settings

```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

15. To load the media files to S3 bucket

- Go to your S3 bucket page on AWS. Create new folder "media"
- go to the media folder and click Upload

[Back to top](#table-of-contents)

## Credits

 ### Code

 For the porpouse of developing this proyect i had to look into some youtube tutorials and web sites.

  * #### Databases relationships
   
      -Video tutorial [Entity Database Relationships](<https://www.youtube.com/watch?v=QpdhBUYk7Kk&list=PLHtuMzYFHMqz4h2gnFL44VZRt0s0HGxN4&index=1>)
  

  * #### Social Authentication

      -Video tutorial [Social Authentication](<https://www.youtube.com/watch?v=-TUEM2NCuVE&list=PLHtuMzYFHMqwVa6AglqPNMShrkySsfPTY&index=7&t=308s>)

  * #### Stripe

  - All the code to implement **Stripe** is taken from the walk through Boutiue Ado with [Code Institute](https://codeinstitute.net/ie/), i never copied and paste away, i wrote everyting by following my notes or the video lessons when needed.

  ### Media

  - Products pictures were taken from different stores, which is why they are differrent sizes and changes the layout in certain card products.

  - Home page images were taken from [Google images](<https://images.google.com/>)

# Aknowlegments

I want to thank the [Code Institute](https://codeinstitute.net/ie/) tutor assistance team, which helped me out with some of the day to day code issues. I could have never complete this project without them!

I did not make use of my mentor assistance this time round. 


[Back to top](#table-of-contents)