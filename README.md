# PetPals App

## Scope:
PetPals is a social media oriented, full-stack web application that connects pet owners by means of sharing images of their pets. Using Django, Python, Javascript, jQuery, HTML, and CSS, our goal is to create an application that allows users to sign-up, create a profile for their pet, post pictures of their pets, and interact with other users through likes and comments. Users will be able to add friends and explore random photos of pets.

## Getting Started
To run an instance of Pet Pals on your local machine, clone the repository, then run:

`python3 manage.py makemigrations`

`python3 manage.py migrate`

`python3 manage.py runserver`

## Built With
**Django/Python** - Web framework used to provide structure to web apps, enabling creation of dynamic, safe websites with managed data storage

**Javascript/JQuery** - Generates likes, follows, and hover effects, powering the frontend

**HTML/CSS** - Frontend structure and styling

**PostgreSQL** - Database Management System, used for storing app state, such as posts, comments, follows, and likes

## Users:
 Our target users are proud pet parents looking to share pictures of their pets and connect with other pet parents via a new, unique social media platform. 

## Features
* Create accounts on PetPals with forms that will ensure proper input, and backend validation of forms
* Edit and customize your profile
* Upload custom pictures of your pets
* Comment on and 'like' pet photos of other users who you follow
* See which other users have liked your photos
* Explore page allows users to see randomly selected photos


## User Story: 

* A user will visit our homepage where they have an option to sign-in or sign up for PetPals 
 * A first-time user will select the ‘sign up’ link which will bring them to a form requesting user to input a username,  email-address, and password that is validated and confirmed. 
  * When preliminary sign-up data is submitted, the user will be redirected to a profile page where they can optionally complete a profile customized with a profile picture and bio
* If the user selects the  ‘sign-in’ button, they will be redirected to their furry-friend feed containing images that have been posted by other accounts that the user is following
 * If a user does not have friends, their feed will appear empty, and the user can visit the ‘Explore’ page that all posts pictures from all members of the Pet Pal community
 * Users can select icons from the nav bar containing links to:  
  * Profile: 
    * User’s profile page that shows user information, posts, whcih may be edited and updated 
  * Explore
    * Features pictures of posts from Pet Pals community
  * Post
    * User can create a posts with a captions to upload a photo of pets to their profile
  * Feed
    * User will see uploaded photos of pets friends that can be interacted with through by liking or commenting on a photo
    * If a user clicks on the name that has been ‘posted by’, the user will be brought to the account that has been clicked ons’ profile page.
    * A like count and comments feed and form will appear for each post
     * If the user clicks on the heart icon in the nav bar, they will be redirected to the likes page where the user can view other accounts that have liked their posts in the format 
    * When the user clicks on an the icon of their profile picture in the nav bar, a logout field will dropdown so user can logout and they will be brought back to the homepage
  
            
### Development Improvment Opportunites
* Add feature to edit/delete comments/posts
* Prevent page reload when comment is submitted using .AJAX request
* Give user option to 'like' or 'comment' on explore page, or user posts
* Create option to edit username
* Improve likes and follows to hold value when page is refreshed
* Reformat hover effects to hold long text captions
* When clicking on picture from another users profile, enlarge image
* Make invalid login credentials appear on screen instead of opening in a new window for login screen
* When a page is blank, add text to tell user what should be on that page 
* Create a more helpful error messages for server/database errors
* Add tooltips to navbar

### Future Wish List
* Implement @mentioning by username
* Implement ability to tag posts 
* Allow users to react in emojis
* Send notifications to users informing them when another user likes or comments on their posts
* Allow user to upload short videos of their pets
* Create nested comment feature, allowing users to comment on comments
* Implement private messaging functionality between pet-parents
* Create a page for users to meet at pet-friendly locations by querying Yelp API for pet-friendly restaurants, dog-parks, or pet stores within set current location range.
* Password recovery options 
* Search bar implementation to find accounts that the user is following

## Links

### Wireframes
[Dropbox link to wireframes](https://www.dropbox.com/s/24iflm7dn3n6ups/PetPals.pdf?dl=0)

### Authors
* [Andrea Piazza](https://github.com/aza024)
* [Luke Engle](https://github.com/Cyrusluke925)
* [Natalie Poulson](https://github.com/natalie-poulson)

### Herkou Link
[Pet Pals on Heroku](https://petpalsproject.herokuapp.com/)

### Acknowledgments
Special thanks to our instructors, Justin Castilla and Dalton Hart for assisting us with this project. 

Thanks to [Pexels.com](https://www.pexels.com) for all stock images!

