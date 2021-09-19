# Welcome to Pulchra Libri

Pulchra Libri is an E-commerce store whose aim is to bring beautifully crafted books to people who love to read.
Users can purchase books as a guest or register.
Registered users will be able to access their profile page to view their previous purchases.

[Link to my deployed site on Heroku](https://darian-pulchra-libri.herokuapp.com/)

# User Experience (UX)

## User Stories

### First Time Visitor Goals
1. Upon first visiting the site, I want to understand what the site is for
2. Easily navigate through the site
3. Quickly create a user account if I think I will use the site again for future purchases
4. Easily make purchases with or without being a registered user
5. Clearly find products for sale and find more information about these before adding to my basket
6. Search for a particular product or only view products of a particular category
7. Sort products by category, price and ratings

### Registered User Goals
1. Easily log in and out of my account
2. Reset my password if I forget it
3. Save my preferred delivery information on my profile for quicker, more convenient checkout
4. View details of my past orders
5. Receive a verification email when creating my account for extra security
6. Receive confirmation that my order has been successful after checkout
7. Be confident that the payment method used is secure
8. Sort products by category, price and ratings
9. Search for a particular product or only view products of a particular category

### Guest User Goals
1. Easily checkout without need to create an account
2. Make a purchase by inputting my delivery information at the checkout
3. Receive confirmation that my order has been successful after checkout
4. Be confident that the payment method used is secure
5. Sort products by category, price and ratings

### Admin/Owner Goals
1. Feel confident a user can easily navigate the site to make purchases
2. Easily add, edit or delete items to/from the store
4. Allow users who do not wish to create an account to also make purchases through the site
5. Make users aware and remind them that they can qualify for free shipping if they spend £255.00+ - this encourages users to spend more to take advantage of free shipping offer

## Design

## Colour Scheme

## Typography

## Imagery

[Unsplash](https://unsplash.com/)

## Wireframes

![Landing Page](media/wireframes/images/LandingPage.png "Landing Page")

![Profile](media/wireframes/images/ProfilePage.png "Profile Page")

![Product Page](media/wireframes/images/ProductPage.png "Product Page")

![Book Description Page](media/wireframes/images/BookDescriptionPage.png "Book Description Page")

![Basket checkout Page](media/wireframes/images/BasketCheckoutPage.png "Basket checkout Page")

![Shopping bag Page](media/wireframes/images/ShoppingBagPage.png "Shopping bag Page")

![Manage Products Page](media/wireframes/images/ManageProductPage.png "Manage Products Page")


# Technologies Used

Languages used for this site:

- [JavaScript](https://www.javascript.com/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Python](https://www.python.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/)

## Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
   - Google fonts were used to import the Roboto font 
2. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used for icons that appear on the site
3. [GitHub:](https://github.com/)
   - GitHub was used to store the project and version control
4. [Wire Frame Sketcher:](https://wireframesketcher.com/)
   - Balsamiq was used to create the wireframes for the site
5. [Heroku:](https://www.heroku.com/)
   - Heroku was used to deploy the site
6. [MongoDB:](https://www.mongodb.com/cloud/atlas)
   - MongoDB used to store data in collections
7. [Unsplash:](https://unsplash.com/)
   - Unsplash for the free images.
8. [Bootstarp:](https://getbootstrap.com/)
   - Frameworks for building clean responcive sites.
9. [jQuery:](https://jquery.com/)
   - jQuery is a fast, small, and feature-rich JavaScript library.


# Features

## Sitewide

### Nav Bar
* The navbar collapses at the Bootstrap medium breakpoint and below. It can be expanded by clicking the collapsed nav icon to access the nav-links.
* Main nav items have a hover effect active which makes the text slightly lighter.
* Dropdown nav items have a hover effect which makes the text slightly lighters.

### Banner
* The site banner shows to free delivery threshold.

### Footer
* The footer contains social media links and is at the bottom of each page.

## Homepage
* The home page features a call-to-action button which is labelled 'Shop Now!'. This button, when clicked, will render the products.html template. Displaying all books within Pulchra Libri's catalogue to the user.

   # Data Structure

   # Testing

## Code Validation

### HTML

---

### CSS

---

### Python

---

### JavaScript

## Testing User Stories from User Experience (UX) Section and Testing

## First Time Visitor Goals

## Returning Time Visitor Goals & Frequent Time Visitor Goals

## Further Testing

# Bugs/Known Issues

# Resolved Issues

# Lighthouse diagnostic results

# Deployment

## Github & Gitpod

1. I created a repository for the project on GitHub, using Gitpod I was able to use the green 'Gitpod' button to open the project in a Gitpod workspace and work on the project from here - commits and pushes were actioned using the source control tab in Gitpod
2. To clone the repository, a user can clone the repo use the 'code' button in the repo. From here the repo can be cloned using HTTPS or GitHub CLI. Alternatively, a user can clone the repo locally by selecting the 'Open with GitHub Desktop' option, this will produce a prompt for GitHub Desktop to open - more information about cloning a repository can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
3. When running locally, all the relevant dependencies will need to be installed using pip, in the IDE's terminal type:
   > pip3 install -r requirements.txt
4. Create a Procfile, this will allow Heroku to understand the type of app we are running, the following should be input to the Procfile:
   > web: gunicorn pulchra_libri.wsgi:application

## Heroku


1. Create a Heroku account or log in if you already have an account
2. Create a new app in Heroku and select your region or closet region, for me this was Europe, I am based in the UK
3. Navigate to 'Resources' and provision a Heroku Postgres database, using the free plan here is fine
4. In GitPod install dj_database_url and psycopg2-binary using the pip3 install command in the terminal
5. Install requirements using
  > pip3 freeze > requirements.txt
6. Import dj_database_url in project level settings.py
7. Comment out the current DATABASE settings(these will be required later) 
8. Obtain DATABASE_URL from Heroku Key Vars, type the following into DATABASE settings 
  > 'default': dj_database_url.parse(*DATABASE URL GOES HERE*)
9. Run migrations by using
  > python3 manage.py migrate
10. If you do not already have a superuser account, you can create one using the following command and following prompts in the terminal
  > python3 manage.py createsuperuser
11. In settings.py uncomment the previously commented out DATABASE settings and update this using an if statement - the app will run on Heroku but can 'fall back' on SQL if needed
12. Install gunicorn using:
  > pip3 install gunicorn
13. Again, freeze requirements using:
  > pip3 freeze > requirements.txt
14. Create Procfile and input the following to allow Heroku to understand how to run the project:
  > web: gunicorn pulchra_libri.wsgi:application
15. Login to Heroki using the terminal by typing and following terminal prompts
  > heroku login -i
16. We do not want Heroku to collect static files so must disable this for now using(--app nandi-store is only requirement if you have one than one app):
  > heroku config:set DISABLE_COLLECTSTATIC=1 --app darian-pulchra-libri
17. Back in settings.py we need to change ALLOWED_HOSTS to, to allow Heroku app to run but also to allow us to still access it via GitPod:
  > ALLOWED_HOSTS = ['darian-pulchra-libri.herokuapp.com', 'localhost']
18. Copy Environment Variables from GitPod into Heroku's Config Vars which can be found in settings

### Deploying in Heroku

1. Using GitPod Heroku needs to be initialised, in the terminal input:
  > git remote: heroku git:remote -a darian-pulchra-libri
2. Push to Heroku main using:
  > git push heroku main
3. In the Heroku Overview you will be able to see Heroku building the app - the site is now live
4. Once Heroku has finished the build, we can link our Git repo to Heroku for automatic deployment which means any changes to the repo will automatically be pushed to the Heroku branch and live site will reflect and changes - In the Deploy tab, click 'GitPod' in Deployment methods and search for the relevant repo and connect
5. Finally, tick the option to allow automatic deploys
6. The app can be launced using the'Open App' button towards the top of the screen

# Credit
