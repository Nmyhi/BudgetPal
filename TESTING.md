# BugetPal - TESTING

This is a memory game web application which is fully responsive. This site has been built to showcase my initial javaScript skills as my very first JavaScript code!

![Am I responsive]()

[View BudgetPal on Heroku ]()

---

## CONTENTS

* [BugetPal - TESTING](#bugetpal---testing)
  * [CONTENTS](#contents)
  * [AUTOMATED TESTING](#automated-testing)
    * [ PEP8 validation](#pep8-validation)
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

###  PEP8 validation

[init_py_validation](/budgetpal/static/images/init_py_validation.png)
[run_py_vlidation](/budgetpal/static/images/run_py_validation.png)
[forms_py_valiation](/budgetpal/static/images/forms_py_validation.png)
[models_py_validation](/budgetpal/static/images/models_py_validation.png)
[routes_py_validation](/budgetpal/static/images/routes_py_validation.png)

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
  - Google pixel 7a

Each device tested the site using the following browsers:

- Google Chrome

Additional testing was taken by friends and family on a variety of devices and screen sizes.

| Feature                                                                     | Expected Outcome                                                                    | Testing Performed                            | Result                                                                                                                        | Pass/Fail |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------- |
| `Home page`                                                                 |
| Navbar Brand logo                                                           | Redirects to the home page                                                          | Click the brans logo                         | redirects to the home page                                                                                                    | Pass      |
| Navbar Home link                                                            | Redirects to the home page                                                          | Click the link                               | redirects to the home page                                                                                                    | Pass      |
| Navbar User link                                                            | Redirects to the user page                                                          | Click the link                               | redirects to the user page                                                                                                    | Pass      |
| Navbar login link                                                           | Redirects to the login page if there is no user logged in                           | Click the link                               | redirects to the login page                                                                                                   | Pass      |
| Navbar logout link                                                          | logs the user out if there is one logged in                                         | Click the link                               | logs the user out                                                                                                             | Pass      |
| Navbar Register                                                             | Redirects to the registration page                                                  | Click the link                               | redirects to the registration page                                                                                            | Pass      |
| Display and welcome the user if one is logged in                            | Check Home page after login                                                         | Welcomes the user                            | Welcomes the user after login                                                                                                 | Pass      |
| Warning of no user logged in                                                | Warns the user to log in                                                            | Check the Home page when nobody is logged in | Warns the user to log in                                                                                                      | Pass      |
| Display log out link if a user is logged in and log out the user if clicked | logs the user out when logout is clicked                                            | Click the link                               | logs the user out                                                                                                             | Pass      |
| Footer-Facebook logo                                                        | Opens my facebook page in a new tab                                                 | Click the facebook logo                      | Opens my facebook page in a new tab                                                                                           | Pass      |
| Footer-mail logo                                                            | Opens sending mail in a new tab                                                     | Click the mail logo                          | opens mails in a new tab                                                                                                      | Pass      |
| Footer-Whatsapp logo                                                        | Opens my whatsapp contact in a new tab                                              | Click the whatsapp logo                      | Opens my whatsapp contact in a new tab                                                                                        | Pass      |
| `User page`                                                                 |
| Navbar Brand logo                                                           | Redirects to the home page                                                          | Click the brans logo                         | redirects to the home page                                                                                                    | Pass      |
| Navbar Home link                                                            | Redirects to the home page                                                          | Click the link                               | redirects to the home page                                                                                                    | Pass      |
| Navbar User link                                                            | Redirects to the user page                                                          | Click the link                               | redirects to the user page                                                                                                    | Pass      |
| Navbar login link                                                           | Redirects to the login page if there is no user logged in                           | Click the link                               | redirects to the login page                                                                                                   | Pass      |
| Navbar logout link                                                          | logs the user out if there is one logged in                                         | Click the link                               | logs the user out                                                                                                             | Pass      |
| Navbar Register                                                             | Redirects to the registration page                                                  | Click the link                               | redirects to the registration page                                                                                            | Pass      |
| User page add income button                                                 | Opens the income form, adds an income to the expenses, calculates the balance       | Click the link                               | Opens the income form, adds an income to the expense, calculates the balance after submission                                 | Pass      |
| User page add expense button                                                | Opens the add expense form, adds an expense to the expenses, calculates the balance | Click the link                               | Opens the add expense form, adds an expense to the expenses, calculates the balance after submission                          | Pass      |
| User page add category button                                               | Opens the add category form, adds a new category to the categories                  | Click the link                               | Opens the add category form, adds a new category to the categories after submission                                           | Pass      |
| User page logout button                                                     | Logs the user out                                                                   | Click the link                               | Logs the user out                                                                                                             | Pass      |
| Footer-Facebook logo                                                        | Opens my facebook page in a new tab                                                 | Click the facebook logo                      | Opens my facebook page in a new tab                                                                                           | Pass      |
| Footer-mail logo                                                            | Opens sending mail in a new tab                                                     | Click the mail logo                          | opens mails in a new tab                                                                                                      | Pass      |
| Footer-Whatsapp logo                                                        | Opens my whatsapp contact in a new tab                                              | Click the whatsapp logo                      | Opens my whatsapp contact in a new tab                                                                                        | Pass      |
| `Login page`                                                                |
| Navbar Brand logo                                                           | Redirects to the home page                                                          | Click the brans logo                         | redirects to the home page                                                                                                    | Pass      |
| Navbar Home link                                                            | Redirects to the home page                                                          | Click the link                               | redirects to the home page                                                                                                    | Pass      |
| Navbar User link                                                            | Redirects to the user page                                                          | Click the link                               | redirects to the user page                                                                                                    | Pass      |
| Navbar login link                                                           | Redirects to the login page if there is no user logged in                           | Click the link                               | redirects to the login page                                                                                                   | Pass      |
| Navbar Register                                                             | Redirects to the registration page                                                  | Click the link                               | redirects to the registration page                                                                                            | Pass      |
| Login page                                                                  | Logs the user in using email address and password                                   | Fill the form up and login                   | Logs the user in using email address and password, remember me has to be clicked on, unfortunately not displaying after click | Pass      |
| Footer-Facebook logo                                                        | Opens my facebook page in a new tab                                                 | Click the facebook logo                      | Opens my facebook page in a new tab                                                                                           | Pass      |
| Footer-mail logo                                                            | Opens sending mail in a new tab                                                     | Click the mail logo                          | opens mails in a new tab                                                                                                      | Pass      |
| Footer-Whatsapp logo                                                        | Opens my whatsapp contact in a new tab                                              | Click the whatsapp logo                      | Opens my whatsapp contact in a new tab                                                                                        | Pass      |
| `Register page`                                                             |
| Navbar Brand logo                                                           | Redirects to the home page                                                          | Click the brans logo                         | redirects to the home page                                                                                                    | Pass      |
| Navbar Home link                                                            | Redirects to the home page                                                          | Click the link                               | redirects to the home page                                                                                                    | Pass      |
| Navbar User link                                                            | Redirects to the user page                                                          | Click the link                               | redirects to the user page                                                                                                    | Pass      |
| Navbar login link                                                           | Redirects to the login page if there is no user logged in                           | Click the link                               | redirects to the login page                                                                                                   | Pass      |
| Navbar Register                                                             | Redirects to the registration page                                                  | Click the link                               | redirects to the registration page                                                                                            | Pass      |
| Register page                                                               | Registers the user using email address and password, confirm password               | Fill the form up and Register                | Registers the user using email address and password, confirm password                                                         | Pass      |
| Footer-Facebook logo                                                        | Opens my facebook page in a new tab                                                 | Click the facebook logo                      | Opens my facebook page in a new tab                                                                                           | Pass      |
| Footer-mail logo                                                            | Opens sending mail in a new tab                                                     | Click the mail logo                          | opens mails in a new tab                                                                                                      | Pass      |
| Footer-Whatsapp logo                                                        | Opens my whatsapp contact in a new tab                                              | Click the whatsapp logo                      | Opens my whatsapp contact in a new tab                                                                                        | Pass      |

## BUGS

### Known Bugs

- On the login page the remember me has bo be clicked on however after the click it is not visible

### Solved Bugs

- Flask- login issues
- category logo url issues
- responsive design issues
- model issues

All of these bugs have been resolved during developement and commits have been created.
