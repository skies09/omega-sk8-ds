# **Omega Skate**
***

[![Build Status](https://travis-ci.org/skies09/omega-sk8-ds.svg?branch=master)](https://travis-ci.org/skies09/omega-sk8-ds)


## Deployment  : https://omega-sk8-ds.herokuapp.com/


## Description

Omega Skate is an online skateboard shop completely focused to skateboards.
Anyone can purchase complete skateboard setups as well as skateboard parts such as decks, trucks, wheels and accessories for skateboards and skateboarding.

---

### UX

The website has been designed similar to other skateshops, however the main difference is the categories on other sites contain other recreational sporting goods or clothing. 

Omega Skate focuses solely on skateboards! For the skateboarding enthusiasts.

---

### Features

### How the website is setup


The body of the website is set up into:

#### Navigation Bar

Contains a search bar at top left. Also includes the website __brand__. The user icon when clicked displays register and login options if the user/customer is not logged in. When the customer is logged in, the user icon displays the profile page. There is also a log out option.
A cart icon is also present and displays cart quantity if products have been added to the cart.

#### Category Banner

This banner contains links to all the categories.

#### Brand Carousel

This carousel slides through images of different skateboard brands.

#### Sale / Promotion Banner

Displays promotions and coupon discounts.

#### Section content

The table below shows what is includes in the block content section on each page.

|Page         |  Block content|
|-------------|-----------------|
|Home         |This page shows links to the different categories of products. There is also a banner and search function.|
|Categories   |Each of the category pages show the different products relating to the category.|
|Product Item |The products page includes descriptions, price and option to purchase/ add to cart.|
|About Us |This page contains infomation regarding the owners of Omega Skate.|
|Deliveries and Returns |This page contains information regarding deliveries and returns.|
|Contact Us   |The contact page contains information on ways the store can be contacted. It also has a form that can be used to message the store. |   
|Help         |The help page contains frequently asked questions. The answers to the questions can be viewed by clicking on the plus icon.|
|Complete Setup Guide |The complete setup guide is an information page which contains details to buying the right size of skateboard. It also contains information for if customers wish to custom build their own skateboard to their specification.|
|Skate Blog   |This links to a skate blog.|
|Profile      |The profile page contains the users email address.|
|Cart         |The cart page shows all the items in the cart with the total for the items and a checkout option. There is an option to amend the products in the cart and an option to remove the item completely from the cart. There is also form to use/submit coupons. |
|Checkout     |The checkout page shows the cart items followed by a form to fill in to submit payment for the items. Payments are managed with Stripe.|


#### Footer

Contains links to pages:
* About us
* Deliveries and Returns
* Contact page
* Help page
* Complete skateboard setup guide
* Skate Blog

Also contains social media links.
*Please note the social links are empty links until set up.*

---

### Extras

#### Features left to implement
* Add an order tracking page.
* Add a star rating system to the products along with review options.
* A wishlist option
* Dropdowns for multiple sizes of decks, wheels and trucks.
---

### Expansion strategy
* Add skate shoes category.
* Add skate clothing category.

---

## Technologies Used
* Bootstrap 3.3.7
* boto3==1.9.139
* botocore==1.12.139
* cdnjs cloudflare
* certifi==2019.3.9
* chardet==3.0.4
* dj-database-url==0.5.0
* Django==1.11
* django-forms-bootstrap==3.1.0
* django-storages==1.7.1
* docutils==0.14
* Font Awesome==4.7.0
* Google fonts
* gunicorn==19.9.0
* idna==2.8
* jmespath==0.9.4
* jQuery 3.3.1
* Pillow==5.4.1
* psycopg2-binary==2.8.3
* python-dateutil==2.8.0
* pytz==2019.1
* s3transfer==0.2.0
* six==1.12.0
* stripe==2.27.0
* urllib3==1.24.2
---

## Deployment  : 
An online demo of the site can be found here: https://omega-sk8-ds.herokuapp.com/



#### Running the project

1. Clone the git repository.
2. CD into cloned repository.
3. Install the requirements with `sudo pip-r requirements.txt`
4. Attempt to run project and get error message. Copy host name and add to "ALLOWED_HOSTS" in settings.py file.
5. Setup of enviroment variables.
* 'STRIPE_PUBLISHABLE'
* 'STRIPE_SECRET'
* 'DATABASE_URL'
* 'SECRET_KEY'
* 'AWS_ACCESS_KEY_ID'
* 'AWS_SECRET_ACCESS_KEY'
6. Setup superuser with `python3 manage.py createsuperuser`
7. Run `python3 manage.py runserver` and view in generated localhost URL.

#### Heroku Deployment

To deploy to Heroku:

1. Create requirements.txt file.
2. Create Procfile.
3. Create Heroku app.
4. From Heroku, click deploy from github repository.
5. Set Config Vars in Heroku as follows:

|**Key**         |  **Value**   |
|-------------|-----------------|
|AWS_ACCESS_KEY_ID     |The AWS Access Key        |
|AWS_SECRET_ACCESS_KEY |The Secret AWS Access Key |
|DATABASE_URL          |The Database Url          |
|DISABLE_COLLECTSTATIC |1                         |
|SECRET_KEY            |The Secret Key            |
|STRIPE_PUBLISHABLE    |The Stripe Publishable Key|
|STRIPE_SECRET         |The Stripe Secret Key     |

6. In Heroku, deploy master branch.
###### The site is now deployed.

---

### Acknowledgements
Products taken from:
* surfdome.com
* noteshop.co.uk
* skatehut.com

#### A special thanks to the mentors and the CodeInstitue Slack Community for all their help.
---