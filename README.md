![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# __Coderscave - Portfolio Project 4__
Welcome to my 4th Project for Code Institute this is a Full-Stack project which involves HTML, CSS, JavaScript, Python +Django and Postgres, this project is deployed through [Heroku](https://heroku.com/).

Coderscave is a restaurant based website which caters for those looking for a better working atmosphere rather than working from home, if this is you come join us!

![amiresponsive](static/img/testing/amiresponsive.png)

## __Live Site__

The deployed project can be found here - [Coderscave](https://coders-cave-project-4.herokuapp.com/)

## __Table of Contents__
- [UX & Design](#ux--design)
    - [User Stories](#user-stories)
        - [New User](#new-user)
        - [Existing User](#existing-user)
        - [Site Admin](#site-admin)
    - [Wireframes](#wireframes)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
- [Features](#features)
    - [Logo and Navigation](#logo-and-navigation)
        - [Normal User](#normal-user)
        - [Superuser](#superuser)
    - [Hero Image](#hero-image)
    - [Footer](#footer)
    - [Review Form](#review-form)
        - [User not logged in](#user-not-logged-in)
        - [User logged in](#user-logged-in)
        - [Review submitted](#review-submitted)
        - [Draft Review](#draft-review-superuser-only)
        - [Published Review](#published-review)
        - [Review Email](#review-email)
    - [Booking Form](#booking-form)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)

## __UX & Design__
&nbsp;  
### __User Stories__
&nbsp;  
#### __New User__
- As a new user I can sign up so that I can access features only registered users can `(MUST HAVE)` &nbsp;  

#### __Existing User__
- As a user I can sign in so that I can book for a table and add a review `(MUST HAVE)`
- As a user I can reset my password so that I can change my password when I cannot remember it `(MUST HAVE)`
- As a user I can easily navigate the homepage so that I can get to the correct part of the website with ease `(MUST HAVE)`
- As a user I can view my bookings so that I can see when my bookings are `(MUST HAVE)`
- As a user I can update my booking so that I can change them depending on availability `(MUST HAVE)`
- As a user I can delete my booking so that I can cancel them if i cannot make it anymore `(MUST HAVE)`
- As a user I can add a review so that give feedback about my booking `(MUST HAVE)`
- As a user I can view other peoples review so that I can see past experiences `(MUST HAVE)`
- As a user I can get a booking confirmation email so that I can remember when my booking is `(SHOULD HAVE)`
- As a user I can get an email regarding booking update so that I can remember the new booking details `(SHOULD HAVE)`
- As a user I can get a cancellation email so that I can confirm my booking is cancelled `(SHOULD HAVE)`
- As a user I want to be able to view email that is designed and not just basic text so that I have a better user experience `(COULD HAVE)`
- As a usr I want to be able to navigate back to the website from the email sent to me so that I can get back to the website with ease `(COULD HAVE)`
- As a user I can receive an email confirmation when my review is publish so that I am aware that my review has been confirmed `(COULD HAVE)`
- As a user I can like/unlike reviews so that i can interact with other users `(WONT HAVE)`
- As a user I can update my review so that I can modify my comments `(WONT HAVE)`
- As a user I can delete a review so that I can delete my review `(WONT HAVE)`

#### __Site Admin__
- As a site admin I can see all bookings so that I can see how many people are booked `(MUST HAVE)`
- As a site admin I can see all drafted reviews so that I can publish them `(MUST HAVE)`
- As a site admin I can publish reviews so that they can be seen by users `(MUST HAVE)`
- As a site admin I can update or delete use bookings so that I can do it for the customer when they request it `(SHOULD HAVE)`
- As a site admin I can delete reviews so that I can delete reviews that are not suitable for other users `(SHOULD HAVE)`
- As a Site Admin I can ban users from booking so that if they are not allowed back in the restaurant they cannot book `(WONT HAVE)`

&nbsp;  
### __Wireframes__
&nbsp;  
### __Colour Scheme__
As my project uses [bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) the colour scheme I used are the ones that are provided in their css :root

```css
:root {
    --white: #fff;
    --secondary: #6c757d;
    --dark: #343a40;
}
```

```css
--dark: #343a40;
```
This is used for the background of the navbar and footer.

```css
--secondary: #6c757d;
```
This is used for the colour of the body to seperate it from the navbar and footer.

```css
--white: #fff;
```
This is used for the text colour so that the content can be easily seen in both --dark and --secondary backgrounds.

&nbsp;  
### __Typography__

For the website, I am using [Google Font](https://fonts.google.com/) I decided to use Poppins for the heading text of the website and Neuton for the body text.

At the beginning I wanted to implement Poppins as the font as it is easy to read, I found the font pairings using [Fontjoy](https://fontjoy.com/).

&nbsp;  
## __Features__
&nbsp;  
### __Logo and Navigation__

- The logo and navigation bar appears on every page of the website, Each of the links will send the user to the targeted pages. After the user logs in the "login" text will be replaced with "Hi, (user)!" and a dropdown element will be accessible to see role-based functionality.

![navbar](static/img/testing/navbar.png)

#### __Normal user__:

- As a normal user they will be able to access "My Bookings" which when they book a table, all their bookings will be shown here. Also a log out functionality is available.

![normaluser](static/img/testing/user-logged-in.png)

#### __Superuser__:

- As a superuser the drop down changes to be able to access the "Admin Panel" from the website instead of having to type "/admin" into the url.

- "All Bookings" is the path to see all the bookings made by any user.

- "All Draft Review" is the path to see all the draft reviews submitted by users, in this page the admin and only the admin can publish the reviews.

![adminuser](static/img/testing/admin-logged-in.png)

&nbsp;  
### __Hero Image__

- The hero image is implemented in every page of the website, the text will change depending on which page the user is currently on. For example if the user clicks on the "Menu" page the text title will be "Menu".

![hero-image](static/img/testing/hero-image.png)

&nbsp;  
### __Footer__

- The footer appears in every page across the website (except for the error pages), the footer includes an about us with a brief description and opening times. It also has links to my github and linkedin, the copyright year has a script that will update depending on what year we are currently in.

![footer](static/img/testing/footer.png)

&nbsp;  
### __Review Form__

- The review form can be found in the home page of the website, parameters has been set that the user has to be logged in to be able to access the form this was done by using django's template language ```{% if user.is_authenticated %} ```.

#### __User not logged in__:

![review-not-logged-in](static/img/testing/review-not-logged-in.png)

#### __User logged in__:

![review-logged-in](static/img/testing/review-logged-in.png)

&nbsp;  
#### __Review Submitted__:

- When the user succesfully submit a review, they will be redirected to the success page.

![review-success](static/img/testing/review-logged-in.png)

&nbsp;  
#### __Draft Review__ (Superuser Only):

- When a review has been succesfully been submitted, the superuser can access this by viewing "All Draft Reviews" page. On this page, the user has two functionalities to publish or to delete the review.

- When a non-superuser tries to access this page by typing the path to the page in the url tab they will be redirected to the 403 page. This was achieved by this code: 

```py
if not request.user.is_superuser:
        raise PermissionDenied
```

![draft-review](static/img/testing/draft-review.png)

- When there are no reviews in the database, this will show instead:

![no-reviews](static/img/testing/no-reviews.png)

&nbsp;  
#### __Published Review__:

- When a superuser publishes a draft review, the review can be seen back on the homepage on the bottom of the page. The delete button option is only accessible to superusers, when a non-superuser is looking at the published reviews the delete button will not be visible. When there are multiple reviews published, the container will allow 3 reviews per row then will make new rows below it. So that the homepage will not be too large when there are multiple of reviews published I allowed the container to be scrolled vertically.

![published-reviews](static/img/testing/published-reviews.png)

&nbsp;  
#### __Review Email__:

- When a review gets published the user that submitted the review will be sent an email confirmation that their review has been published and can be seen on the website.

![review-email](static/img/testing/review-email.png)

&nbsp;  
### __Booking Form__

