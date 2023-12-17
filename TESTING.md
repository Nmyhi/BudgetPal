# BugetPal - TESTING

This is a memory game web application which is fully responsive. This site has been built to showcase my initial javaScript skills as my very first JavaScript code!

![Am I responsive]()

[View cogniCraft on github pages ]()

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

[W3C](https://validator.w3.org/) was used to validate the HTML the website. It was also used to validate the CSS.

* [Index Page HTML](assets/images/readme/htmlvalidation.png) - Pass
* [CSS validation](assets/images/readme/cssvalidation.png) - Pass

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

* Index Page mobile view
  ! The Index page Lighthouse results can be found here [Index Page Lighthouse mobile view](assets/images/readme/lighthousemobile.png)

* Index Page desktop view
  ! The Index page Lighthouse results can be found here [Index Page Lighthouse desktop view](assets/images/readme/lighthousedesktop.png)

## MANUAL TESTING

### Testing User Stories

Client Goals

* To navigate in the menu.
* To play the game with no issues.
* To have fun by trying to complete it within the least amount of time.
* To access previously played time record in the High Score menu.
* To access the developer's personal social-media using the footer links.

First Time Visitor Goals

* To navigate in the menu.
* To play the game with no issues.
* To have fun by trying to complete it within the least amount of time.
* To access previously played time record in the High Score menu.
* To access the developer's personal social-media using the footer links.

Returning Visitor Goals

* To navigate in the menu.
* To play the game with no issues.
* To have fun by trying to complete it within the least amount of time.
* To access previously played time record in the High Score menu.
* To access the developer's personal social-media using the footer links.

Frequent Visitor Goals

* To navigate in the menu.
* To play the game with no issues.
* To have fun by trying to complete it within the least amount of time.
* To access previously played time record in the High Score menu.
* To access the developer's personal social-media using the footer links.

I think even for playing the game for the first time the user goals are pretty much the same than the returning and frequently returning user's goals therefore I will do the manual testing against the 5 user goals.

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| To navigate in the menu. | I have achieved this by creating a menu system | [menu system](assets/images/readme/desktopmainmenu.png)
| To play the game with no issues. | I have made the game fully functioning with no bugs  | [gameplay](assets/images/readme/desktopplayarea.png) |
| To have fun by trying to complete it within the least amount of time.| I achieved this by measuring the time and saving the username , time into the localstorage and display it in the highscore menu | [gameplay](assets/images/readme/ingamescreenshot.png) |
| To access previously played time record in the High Score menu. | I have achieved this goal by displaping the user's top-10 scores in the Hi-Scores menu | [high-scores](assets/images/readme/highscorescreenshot.png) |
| To access the developer's personal social-media using the footer links. | I have achieved this goal by displaying the social media links in the footer | [Social links](assets/images/readme/footerscreenshot.png) |

### Full Testing

Full testing was performed on the following devices:

* Laptop:
  * hp pavilion 15" laptop
* Mobile Devices:
  * iPhone 13 pro.
  * Samsung galaxy S10.
  * Samsung galaxy A22.

Each device tested the site using the following browsers:

* Google Chrome

Additional testing was taken by friends and family on a variety of devices and screen sizes.

Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| `Main menu` |
| Play Button | Makes the javaScript code to populate the DOM with the game area content | Click Play button | Enters the game area | Pass |
| High-Scores button | Makes the javaScript code to populate the DOM with the high score data | Click High-Scores button | Enters the High-Scores area | Pass |
| Help button | Makes the javaScript code to populate the DOM with the help data | Click Help button | Enters the Help area | Pass |
| Footer-Facebook logo | Opens my facebook page in a new tab | Click the facebook logo | Opens my facebook page in a new tab | Pass |
| Footer-Instagram logo | Opens my instagram page (which is about my lasercutting business) in a new tab | Click the instagram logo | Opens my instagram page in a new tab | Pass |
| Footer-Whatsapp logo | Opens my whatsapp contact in a new tab | Click the whatsapp logo | Opens my whatsapp contact in a new tab | Pass |
| `Play` |
| Menu Button | Refreshes the index.html | Click Menu button | "Takes back" to the main menu | Pass |
| Username Input | Takes the username , no spaces only and maximum 15 characters. After hitting enter it displays the username in the top left corner and starts a timer which is displayed in the top right corner | Enter a valid username and check if it is displayed and it starts the timer | It takes and displays the username and starts the timer | Pass |
| Save&Reset button(appeares after completing a game) | Saves the highscore and time and then resets the page | Click Save&Reset button | Saves the score and resets the page | Pass |
| Footer-Facebook logo | Opens my facebook page in a new tab | Click the facebook logo | Opens my facebook page in a new tab | Pass |
| Footer-Instagram logo | Opens my instagram page (which is about my lasercutting business) in a new tab | Click the instagram logo | Opens my instagram page in a new tab | Pass |
| Footer-Whatsapp logo | Opens my whatsapp contact in a new tab | Click the whatsapp logo | Opens my whatsapp contact in a new tab | Pass |
| `High-Scores` |
| Menu Button | Refreshes the index.html | Click Menu button | "Takes back" to the main menu | Pass |
| Footer-Facebook logo | Opens my facebook page in a new tab | Click the facebook logo | Opens my facebook page in a new tab | Pass |
| Footer-Instagram logo | Opens my instagram page (which is about my lasercutting business) in a new tab | Click the instagram logo | Opens my instagram page in a new tab | Pass |
| Footer-Whatsapp logo | Opens my whatsapp contact in a new tab | Click the whatsapp logo | Opens my whatsapp contact in a new tab | Pass |
| `Help` |
| Menu Button | Refreshes the index.html | Click Menu button | "Takes back" to the main menu | Pass |
| Footer-Facebook logo | Opens my facebook page in a new tab | Click the facebook logo | Opens my facebook page in a new tab | Pass |
| Footer-Instagram logo | Opens my instagram page (which is about my lasercutting business) in a new tab | Click the instagram logo | Opens my instagram page in a new tab | Pass |
| Footer-Whatsapp logo | Opens my whatsapp contact in a new tab | Click the whatsapp logo | Opens my whatsapp contact in a new tab | Pass |


## BUGS

### Known Bugs

There is no known bugs at the moment.

### Solved Bugs

* The username window input did not have a whitespace validation.
* The username window input had no characters limit.
* The username window was not responsive enough.
* The game did not store the high score data.

All of these bugs have been resolved during developement and commits have been created.