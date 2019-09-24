# **Omega Skate**

***

[![Build Status](https://travis-ci.org/skies09/omega-sk8-ds.svg?branch=master)](https://travis-ci.org/skies09/omega-sk8-ds)
---

## Deployment  : https://omega-sk8-ds.herokuapp.com/

---

#### Running the project

1. Clone the git repository.
2. CD into cloned repository.
3. Install the requirements with `sudo pip-r requirements.txt`
4. Attempt to run project and get error message. Copy host name and add to "ALLOWED_HOSTS" in settings.py file.
5. Setup of enviroment variables.
..* 'STRIPE_PUBLISHABLE', ''
..* 'STRIPE_SECRET', ''
..* 'DATABASE_URL', ''
..* 'SECRET_KEY', ''
..* 'AWS_ACCESS_KEY_ID', ''
..* 'AWS_SECRET_ACCESS_KEY', ''
6. Setup superuser.
###### Run `python3 manage.py runserver` and view in generated localhost URL.

#### Heroku Deployment

To deploy to Heroku:

1. Create requirements.txt file.
2. Create Procfile.
3. Create Heroku app.
4. From Heroku, click deploy from github repository.
5. Set Config Vars in Heroku as follows:
|Key         |  Value   |
|-------------|-----------------|
|AWS_ACCESS_KEY_ID     |<Your AWS Access Key>        |
|AWS_SECRET_ACCESS_KEY |<Your Secret AWS Access Key> |
|DATABASE_URL          |<Your Database Url>          |
|DISABLE_COLLECTSTATIC |1                            |
|SECRET_KEY            |<Your Secret Key>            |
|STRIPE_PUBLISHABLE    |<Your Stripe Publishable Key>|
|STRIPE_SECRET         |<Your Stripe Secret Key      |

6. In Heroku, deploy master branch.
###### The site is now deployed.

---

## Description

---

Omega Skate is an online skateboard shop completely focused to skateboards.
Anyone can purchase complete skateboard setups as well as skateboard parts such as skateboard decks, skateboard trucks, skateboard wheels and accessories for skateboards and skateboarding.


## UX

---

The website has been designed similar to other skateshops, however the main difference is the categories on other sites contain other recreational sporting goods or clothing. Omega Skate focuses solely on skateboards!

## Features

---

### How the website is setup

---

The body of the website is set up into

#### Navigation Bar

Includes the website __brand__ along with register and login options if the user/customer is not logged in, or profile and logout option if user is logged in.
A cart icon is also present and displays cart quantity if products have been added to the cart.

#### Introduction Container

Includes website banner and website title.

#### Section content

The table below shows what is includes in the block content section on each page 

|Page         |  Block content|
|-------------|-----------------|
|Home         |This page shows links to the different categories of products. There is also a banner and search function.|
|Categories   |Each of the category pages show the different products relating to the category. These products include descriptions, price and option to purchase/ add to cart.|
|Deliveries + Returns |This page contains information regarding deliveries and returns.|
|Contact Us   |The contact page contains information on ways the store can be contacted. It also has a form that can be used to message the store.|   
|Help         |The help page contains frequently asked questions. The answers to the questions can be viewed by clicking on the plus icon.|
|Complete Setup Guide |The complete setup guide is an information page which contains details to buying the right size of skateboard. It also contains information for if customers wish to custom build their own skateboard to their specification.|
|Profile      |The profile page contains the users email address.|
|Cart         |The cart page shows all the items in the cart with the total for the items and a checkout option. There is also an option to amend the products in the cart. |
|Checkout     |The checkout page shows the cart items followed by a form to fill in to submit payment for the items.|


#### Footer

Contains links to pages:
* Deliveries + Returns
* Contact page
* Help page
* Complete skateboard setup guide

Also contains social media links.
*Please note the social links are empty links until set up.*

---

### Extras

#### Features left to implement
* A live chat feature to reduce delay in customer service and potentially boost sales.
* Use of discount or promo codes in checkout.
* Connect a skate blog.
* Add an about page which shows the owners of the skate shop, who are skating enthusiasts.
* Add an order tracking page.
---

### Expansion strategy
* Add skate shoes category.
* Add clothing category.

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

