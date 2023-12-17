# BugetPal - TESTING

This is a memory game web application which is fully responsive. This site has been built to showcase my initial javaScript skills as my very first JavaScript code!

![Am I responsive]()

[View BudgetPal on Heroku ]()

---

## CONTENTS

* [BugetPal - TESTING](#bugetpal---testing)
  * [CONTENTS](#contents)
  * [AUTOMATED TESTING](#automated-testing)
    * [ W3C Validator](#w3c-validator)
    * [Lighthouse](#lighthouse)
  * [MANUAL TESTING](#manual-testing)
    * [Testing User Stories](#testing-user-stories)
    * [Full Testing](#full-testing)
  * [BUGS](#bugs)
    * [Known Bugs](#known-bugs)
    * [Solved Bugs](#solved-bugs)

---

## AUTOMATED TESTING

The automated Testing includes all the testing that is carried out by test code like jest, W3C HTML, and CSS validation.

###  W3C Validator

I had issues with validating my html pages because the flask elements.

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

- Index Page mobile view
  ! The Index page Lighthouse results can be found here [Index Page Lighthouse mobile view](assets/images/readme/lighthousemobile.png)

- Index Page desktop view
  ! The Index page Lighthouse results can be found here [Index Page Lighthouse desktop view](assets/images/readme/lighthousedesktop.png)

## MANUAL TESTING

### Testing User Stories

Client Goals

- To help the clients to have a better understanding of their spending.
- To navigate in the menu.
- To be able to view the site on a range of device sizes.
- To allow people to sign up, log in and log out on the site the site.
- To be able to add records of categories, expenses, savings and incomes.
- To be able to modify expenses, savings and incomes.
- To be able to delete expenses, savings and incomes.
- To be able to see the updated Balance and Savings.
- To be able to see the details of the expenses.

First Time Visitor Goals

- To be able to create an account, log in or log out.
- To be able to create read edit and delete expenses.
- To be able to contact the developer in case of ideas to develop the project

Returning Visitor Goals

- To be able to create an account, log in or log out.
- To be able to create read edit and delete expenses.
- To be able to contact the developer in case of ideas to develop the project.

Frequent Visitor Goals

- To be able to create an account, log in or log out.
- To be able to create read edit and delete expenses.
- To be able to contact the developer in case of ideas to develop the project.
- To Gain insights into the user's spending habits and financial patterns to make informed decisions.
- Set achievable financial goals and track your progress toward a secure financial future.

| Goals                                                                   | How are they achieved?                                                                           | Image                                                                              |
| :---------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| To help the clients to have a better understanding of their spending.   | I have achieved this by displaying the expenses and updating the balance and savings of the user | [Userpage](/budgetpal/static/images/userpage_logged_in.png)                        |
| To navigate in the menu.                                                | I have made a nav bar to easily navigate in the menu                                             | [Navbar](/budgetpal/static/images/navbar.png)                                      |
| To allow people to sign up, log in and log out on the site the site.    | I have achieved this by using Flask-login                                                        | [Flask-login documentation](https://flask-login.readthedocs.io/en/latest/)         |
| To be able to add records of categories, expenses, savings and incomes. | I have achieved this by adding buttons to the userpage                                           | [Control buttons on the userpage](/budgetpal/static/images/userpage_logged_in.png) |
| To be able to modify expenses, savings and incomes.                     | I have achieved this goal by adding edit button to the expenses savings and incomes              | [Userpage](/budgetpal/static/images/userpage_logged_in.png)                        |
| To be able to delete expenses, savings and incomes.                     | I have achieved this goal by adding delete button to the expenses savings and incomes            | [Userpage](/budgetpal/static/images/userpage_logged_in.png)                        |
| To be able to see the updated Balance and Savings.                      | I have achieved this goal by displaying these information on the user site                       | [Userpage](/budgetpal/static/images/userpage_logged_in.png)                        |
| To be able to see the details of the expenses.                          | I have achieved this goal by displaying these informations in the expenses rows                  | [Userpage](/budgetpal/static/images/userpage_logged_in.png)                        |

### Full Testing

Full testing was performed on the following devices:

- Laptop:
  - hp pavilion 15" laptop
- Mobile Devices:
  - iPhone 13 pro.
  - Samsung galaxy S10.
  - Samsung galaxy A22.

Each device tested the site using the following browsers:

- Google Chrome

Additional testing was taken by friends and family on a variety of devices and screen sizes.

| Feature                                             | Expected Outcome                                                                                                                                                                                 | Testing Performed                                                           | Result                                                  | Pass/Fail |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------- | --------- |
| `Main menu`                                         |
| Play Button                                         | Makes the javaScript code to populate the DOM with the game area content                                                                                                                         | Click Play button                                                           | Enters the game area                                    | Pass      |
| High-Scores button                                  | Makes the javaScript code to populate the DOM with the high score data                                                                                                                           | Click High-Scores button                                                    | Enters the High-Scores area                             | Pass      |
| Help button                                         | Makes the javaScript code to populate the DOM with the help data                                                                                                                                 | Click Help button                                                           | Enters the Help area                                    | Pass      |
| Footer-Facebook logo                                | Opens my facebook page in a new tab                                                                                                                                                              | Click the facebook logo                                                     | Opens my facebook page in a new tab                     | Pass      |
| Footer-Instagram logo                               | Opens my instagram page (which is about my lasercutting business) in a new tab                                                                                                                   | Click the instagram logo                                                    | Opens my instagram page in a new tab                    | Pass      |
| Footer-Whatsapp logo                                | Opens my whatsapp contact in a new tab                                                                                                                                                           | Click the whatsapp logo                                                     | Opens my whatsapp contact in a new tab                  | Pass      |
| `Play`                                              |
| Menu Button                                         | Refreshes the index.html                                                                                                                                                                         | Click Menu button                                                           | "Takes back" to the main menu                           | Pass      |
| Username Input                                      | Takes the username , no spaces only and maximum 15 characters. After hitting enter it displays the username in the top left corner and starts a timer which is displayed in the top right corner | Enter a valid username and check if it is displayed and it starts the timer | It takes and displays the username and starts the timer | Pass      |
| Save&Reset button(appeares after completing a game) | Saves the highscore and time and then resets the page                                                                                                                                            | Click Save&Reset button                                                     | Saves the score and resets the page                     | Pass      |
| Footer-Facebook logo                                | Opens my facebook page in a new tab                                                                                                                                                              | Click the facebook logo                                                     | Opens my facebook page in a new tab                     | Pass      |
| Footer-Instagram logo                               | Opens my instagram page (which is about my lasercutting business) in a new tab                                                                                                                   | Click the instagram logo                                                    | Opens my instagram page in a new tab                    | Pass      |
| Footer-Whatsapp logo                                | Opens my whatsapp contact in a new tab                                                                                                                                                           | Click the whatsapp logo                                                     | Opens my whatsapp contact in a new tab                  | Pass      |
| `High-Scores`                                       |
| Menu Button                                         | Refreshes the index.html                                                                                                                                                                         | Click Menu button                                                           | "Takes back" to the main menu                           | Pass      |
| Footer-Facebook logo                                | Opens my facebook page in a new tab                                                                                                                                                              | Click the facebook logo                                                     | Opens my facebook page in a new tab                     | Pass      |
| Footer-Instagram logo                               | Opens my instagram page (which is about my lasercutting business) in a new tab                                                                                                                   | Click the instagram logo                                                    | Opens my instagram page in a new tab                    | Pass      |
| Footer-Whatsapp logo                                | Opens my whatsapp contact in a new tab                                                                                                                                                           | Click the whatsapp logo                                                     | Opens my whatsapp contact in a new tab                  | Pass      |
| `Help`                                              |
| Menu Button                                         | Refreshes the index.html                                                                                                                                                                         | Click Menu button                                                           | "Takes back" to the main menu                           | Pass      |
| Footer-Facebook logo                                | Opens my facebook page in a new tab                                                                                                                                                              | Click the facebook logo                                                     | Opens my facebook page in a new tab                     | Pass      |
| Footer-Instagram logo                               | Opens my instagram page (which is about my lasercutting business) in a new tab                                                                                                                   | Click the instagram logo                                                    | Opens my instagram page in a new tab                    | Pass      |
| Footer-Whatsapp logo                                | Opens my whatsapp contact in a new tab                                                                                                                                                           | Click the whatsapp logo                                                     | Opens my whatsapp contact in a new tab                  | Pass      |

## BUGS

### Known Bugs

There is no known bugs at the moment.

### Solved Bugs

- The username window input did not have a whitespace validation.
- The username window input had no characters limit.
- The username window was not responsive enough.
- The game did not store the high score data.

All of these bugs have been resolved during developement and commits have been created.
