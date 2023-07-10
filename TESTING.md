## __Testing__

Head back to the [README.md](README.md) file.

&nbsp;

## __Introduction__

To make sure that my website is running as intended, I will be using different tools to see its performance.

- Every page will be testing on lighthouse for Desktop and Mobile.
- Every page's HTML will be checked on [W3C Validator](https://validator.w3.org/)
    - For the HTML pages that requires users to be authenticated I will be validating the HTML through direct input using the page source as W3C is not authenticated it will not see my if authenticated template syntax.
- Every page's CSS will be checked on [W3C Validator - Jigsaw](https://jigsaw.w3.org/css-validator/)
- Every Python code will be checked on [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
- Every JavaScript code will be checked on [JShint](https://jshint.com/)

### __Homepage__

[index.html](https://coders-cave-project-4.herokuapp.com/)

|                    | Screenshot                                                        |              Notes                   |
|--------------------|-------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![index-desktop](static/img/testing/lighthouse-index-desktop.png) |                                      |
| Mobile             | ![index-mobile](static/img/testing/lighthouse-index-mobile.png)   | Performance down due to image sizes. |
| W3C HTML Validator | ![index-validator](static/img/testing/index-validator.png)        |                                      |

&nbsp;  
### __Menu__

[menu.html](https://coders-cave-project-4.herokuapp.com/menu/)

|                    | Screenshot                                                        |              Notes                   |
|--------------------|-------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![menu-desktop](static/img/testing/lighthouse-menu-desktop.png)   |                                      |
| Mobile             | ![menu-mobile](static/img/testing/lighthouse-menu-mobile.png)     | Performance down due to image sizes. |
| W3C HTML Validator | ![menu-validator](static/img/testing/menu-validator.png)          |                                      |

&nbsp;  
### __Book__

[bookings.html](https://coders-cave-project-4.herokuapp.com/book/form/)

|                    | Screenshot                                                        |              Notes                  |
|--------------------|-------------------------------------------------------------------|-------------------------------------|
| Desktop            | ![book-desktop](static/img/testing/lighthouse-book-desktop.png)   | Accessibility down due to form having placeholders instead of labels. |
| Mobile             | ![book-mobile](static/img/testing/lighthouse-book-mobile.png)     | Performance down due to image sizes. <br> Accessibility down due to form having placeholders instead of labels. |
| W3C HTML Validator | ![book-validator](static/img/testing/book-validator.png)          |                                     |

&nbsp;  
### __Login__

[login.html](https://coders-cave-project-4.herokuapp.com/accounts/login/)

|                    | Screenshot                                                        |              Notes                   |
|--------------------|-------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![login-desktop](static/img/testing/lighthouse-login-desktop.png) | Accessibility down due to form having placeholders instead of labels. |
| Mobile             | ![login-mobile](static/img/testing/lighthouse-login-mobile.png)   | Performance down due to image sizes. <br> Accessibility down due to form having placeholders instead of labels. |
| W3C HTML Validator | ![login-validator](static/img/testing/login-validator.png)        |                                      |

&nbsp;  
### __Logout__

[logout.html](https://coders-cave-project-4.herokuapp.com/accounts/logout/)

|                    | Screenshot                                                            |              Notes                   |
|--------------------|-----------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![logout-desktop](static/img/testing/lighthouse-logout-desktop.png)   |                                      |
| Mobile             | ![logout-mobile](static/img/testing/lighthouse-logout-mobile.png)     | Performance down due to image sizes. |
| W3C HTML Validator | ![logout-validator](static/img/testing/logout-validator.png)          |                                      |

&nbsp;  
### __Signup__

[signup.html](https://coders-cave-project-4.herokuapp.com/accounts/signup/)

|                    | Screenshot                                                            |              Notes                   |
|--------------------|-----------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![signup-desktop](static/img/testing/lighthouse-signup-desktop.png)   |                                      |
| Mobile             | ![signup-mobile](static/img/testing/lighthouse-signup-mobile.png)     | Performance down due to image sizes. |
| W3C HTML Validator | ![signup-validator](static/img/testing/signup-validator.png)          |                                      |

&nbsp;  
### __Booking List__

[my_booking.html](https://coders-cave-project-4.herokuapp.com/book/bookings/)

|                    | Screenshot                                                            |              Notes                   |
|--------------------|-----------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![booking-desktop](static/img/testing/lighthouse-booking-desktop.png) |                                      |
| Mobile             | ![booking-mobile](static/img/testing/lighthouse-booking-mobile.png)   | Performance down due to image sizes. |
| W3C HTML Validator | ![booking-validator](static/img/testing/booking-validator.png)        |                                      |

&nbsp;  
### __Update Booking__

|                    | Screenshot                                                            |              Notes                   |
|--------------------|-----------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![update-desktop](static/img/testing/lighthouse-update-desktop.png)   | Accessibility down due to form having placeholders instead of labels. |
| Mobile             | ![update-mobile](static/img/testing/lighthouse-update-mobile.png)     | Performance down due to image sizes. <br> Accessibility down due to form having placeholders instead of labels. |
| W3C HTML Validator | ![update-validator](static/img/testing/update-validator.png)          |                                      |

&nbsp;  
### __Delete Booking__

|                    | Screenshot                                                            |              Notes                   |
|--------------------|-----------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![delete-desktop](static/img/testing/lighthouse-delete-desktop.png)   |                                      |
| Mobile             | ![delete-mobile](static/img/testing/lighthouse-delete-mobile.png)     | Performance down due to image sizes. |
| W3C HTML Validator | ![delete-validator](static/img/testing/delete-validator.png)          |                                      |

&nbsp;  
### __All Booking List__

[all_bookings.html](https://coders-cave-project-4.herokuapp.com/book/bookings/all-bookings/)

|                    | Screenshot                                                                    |                      Notes                   |
|--------------------|-------------------------------------------------------------------------------|----------------------------------------------|
| Desktop            | ![all-booking-desktop](static/img/testing/lighthouse-all-booking-desktop.png) |                                              |
| Mobile             | ![all-booking-mobile](static/img/testing/lighthouse-all-booking-mobile.png)   | Performance down due to image sizes.         |
| W3C HTML Validator | ![all-booking-validator](static/img/testing/all-booking-validator.png)        |                                              |

&nbsp;  
### __All Draft Reviews List__

[view_all_draft_reviews.html](https://coders-cave-project-4.herokuapp.com/review/draft-reviews)

|                    | Screenshot                                                                        |                      Notes                   |
|--------------------|-----------------------------------------------------------------------------------|----------------------------------------------|
| Desktop            | ![draft-reviews-desktop](static/img/testing/lighthouse-draft-reviews-desktop.png) |                                              |
| Mobile             | ![draft-reviews-mobile](static/img/testing/lighthouse-draft-reviews-mobile.png)   | Performance down due to image sizes.         |
| W3C HTML Validator | ![draft-reviews-validator](static/img/testing/draft-reviews-validator.png)        |                                              |

&nbsp;  
### __Review Success__

[view_all_draft_reviews.html](https://coders-cave-project-4.herokuapp.com/review/draft-reviews)

|                    | Screenshot                                                                          |                      Notes                   |
|--------------------|-------------------------------------------------------------------------------------|----------------------------------------------|
| Desktop            | ![review-success-desktop](static/img/testing/lighthouse-review-success-desktop.png) |                                              |
| Mobile             | ![review-success-mobile](static/img/testing/lighthouse-review-success-mobile.png)   | Performance down due to image sizes.         |
| W3C HTML Validator | ![review-success-validator](static/img/testing/review-success-validator.png)        |                                              |

&nbsp;  
### __Delete Review__

|                    | Screenshot                                                                |              Notes                   |
|--------------------|---------------------------------------------------------------------------|--------------------------------------|
| Desktop            | ![delete-review](static/img/testing/lighthouse-delete-review-desktop.png) |                                      |
| Mobile             | ![delete-review](static/img/testing/lighthouse-delete-review-mobile.png)  | Performance down due to image sizes. |
| W3C HTML Validator | ![delete-review](static/img/testing/delete-review-validator.png)          |                                      |

&nbsp;  


