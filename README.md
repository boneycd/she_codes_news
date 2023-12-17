# {{ your_name_here }} - She Codes News Project

## About This Project{{ Give a brief description of your project here. What is it for, how do you useit? }}


## How To Run This Code
{{
    STEP 1:
 copy the repo over to your own Github account 

 Next, visit the newly created repo on your Github, and click the "Code" button to getthe url to clone:

 Finally, jump into a terminal and navigate to wherever you've been storing yourprojects so far. Then clone the repo down to your local machine, like so: `git clone <your_link_goes_here>`

    STEP 2:
 In the terminal, change directory into the repo you just cloned down:
 `cd your_repo`

 Now, create a new virtual environment, like so
 `python -m venv venv`

 Then activate the environment:
 Windows command: `.venv/Scripts/activate`
 Mac command:`source venv/bin/activate`

 Now install the requirements:
 `python -m pip install -r requirements.txt`
 
 open the repo in VS Code
 `code .`

    STEP 3 - Make The Initial Migrations

 To make migrations,  change directories so that you're next to the `manage.py` file. 
 Now make the initial migrations: `python manage.py migrate`
 Finally, check that the starter code is working correctly by running the server:`python manage.py runserver`

    }}

## Database Schema
![ {{ My ERD }} ]( {{ ./plus-django-news-project-template\screenshots\ERD.png }} )

## Project Features
[x] Order stories by date
![ Screenshot of Stories displayed in the order of newest to the oldest creation date ]( screenshots/OrderStoriesByDate.png )

[x] Styled "new story" form
![ {{ Screenshot of my "New Story" form }} ]
( {{ ./plus-django-news-project-template\screenshots\StyledNEWSTORYform.png }} )

[x] Story images
![ {{ Screenshot of images in my stories. Added a field to the NewsStory model for an image url and use this image url rather than the default images provided in the starter. }} ]
( {{ ./plus-django-news-project-template\screenshots\StoryImages.png }} )

[x] Log-in/log-out
![ {{ Screenshot of Log-in , Log-out , Write a new story links}} ]
( {{ ./plus-django-news-project-template\screenshots\LoginLogout.png }} )

[x] "Account view" page
![ {{ Screenshot of profile information page , shows three user profiles created for this website  }} ]
( {{ ./plus-django-news-project-template\screenshots\AccountViewPage.png }} )

[x] "Create Account" page
![ {{ Screenshot of Create Account page }} ]( {{ ./plus-django-news-project-template\screenshots\CreateAccount.png }} )

[x] View stories by author
![ {{ Screenshot of stories by the three authors individually}} ]( {{ ./plus-django-news-project-template\screenshots\ViewStoriesByAuthor.png }} )

[x] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
![ {{ Screenshot of the webpage showing -"Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in  }} ]( {{ ./plus-django-news-project-template\screenshots\LoginLogoutButtonVisibility.png}} )

[x] "Create Story" functionality only available when user is logged in
![ {{ Screenshot which shows "Write New Story Form" is only available when the user is logged in , Otherwise it says "Please login to write a new story. }} ]( {{ ./plus-django-news-project-template\screenshots\CreateStoryAvailability.png}} )


## Additional Features:

[x] Add the ability to delete stories (Could not work on permissions part , This is just a page to delete stories).
![ {{ Delete Story link & warning message before submission}} ]( {{ ./plus-django-news-project-template\screenshots\DeleteStory.png }} )