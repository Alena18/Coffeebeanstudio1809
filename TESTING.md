# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

- https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoffeebeanstudio1809-7c1114e7ca53.herokuapp.com%2F

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoffeebeanstudio1809-7c1114e7ca53.herokuapp.com%2F) | ![screenshot](documentation/html.png) | Pass: No Errors  |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoffeebeanstudio1809-7c1114e7ca53.herokuapp.com%2Fbag%2F) | ![screenshot](documentation/htmlbag.png) | Pass: No Errors |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoffeebeanstudio1809-7c1114e7ca53.herokuapp.com%2Fprofile%2F) | ![screenshot](documentation/htmlprofile.png) | Pass: No Errors |
| Product View |[W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoffeebeanstudio1809-7c1114e7ca53.herokuapp.com%2Fdesignproducts%2F%3Fcategory%3Dbanners) | ![screenshot](documentation/productsviewhtml.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcoffeebeanstudio1809-7c1114e7ca53.herokuapp.com%2Fcheckout%2F) | ![screenshot](documentation/htmlcheckout.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2FAlena18.github.io%2FCoffeebeanstudio1809) | ![screenshot](documentation/cssaws.png) | Pass: No Errors |
| checkout.css | [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input)| ![screenshot](documentation/csscheckout.png) | Pass: No Errors |
| profile.css | [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) | ![screenshot](documentation/cssprofile.png) | Pass: No Errors |

### JavaScript

I have used the recommended [Jshint](https://jshint.com/) to validate all of my Javascript files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/stripe.png) | Undefined variable that defines according to stripe website |
| questions.js | ![screenshot](documentation/countryfield.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| manage.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/manage.py) | ![screenshot](documentation/managecof.png) | Pass: No Errors |
| settings.py before validation | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/coffeebeanstudio1809/settings.py) | ![screenshot](documentation/settingbefore.png) | Few errors, all fixed |
| settings.py after validation | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/coffeebeanstudio1809/settings.py) | ![screenshot](documentation/settingafter.png) | Pass: No Errors |
| custom_storages.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/custom_storages.py) | ![screenshot](documentation/customerstorage.png) | Pass: No Errors |
| Coffeebeanstudio1809 url.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/coffeebeanstudio1809/asgi.py) | ![screenshot](documentation/urlcoffee.png) | Pass: No Errors |
| Coffeebeanstudio1809 view.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/coffeebeanstudio1809/views.py) | ![screenshot](documentation/viewcoffee.png) | Pass: No Errors |
| Coffeebeanstudio1809 wsgi.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/coffeebeanstudio1809/wsgi.py) | ![screenshot](documentation/wsgicoffee.png) | Pass: No Errors |
| Bag app.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/bag/apps.py) | ![screenshot](documentation/bagapp.png) | Pass: No Errors |
| Bag context.py before validation| [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/bag/contexts.py) | ![screenshot](documentation/bagcontextbefore.png) | Few errors, all fixed |
| Bag context.py after validation| [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/bag/contexts.py) | ![screenshot](documentation/bagcontextafter.png) | Pass: No Errors |
| Bag url.py after validation| [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/bag/urls.py) | ![screenshot](documentation/bagurl.png) | Pass: No Errors |
| bag view.py after validation| [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/bag/views.py) | ![screenshot](documentation/bagviewpy.png) | Pass: No Errors |
| Checkout admin.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/admin.py) | ![screenshot](documentation/admincheckout.png) | Pass: No Errors |
| Checkout app.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/apps.py) | ![screenshot](documentation/appcheckout.png) | Pass: No Errors |
| Checkout forms.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/forms.py) | ![screenshot](documentation/formscheckout.png) | Pass: No Errors |
| Checkout model.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/models.py) | ![screenshot](documentation/modelcheckout.png) | Pass: No Errors |
| Checkout signals.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/signals.py) | ![screenshot](documentation/signalcheckout.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/urls.py) | ![screenshot](documentation/urlcheckout.png) | Pass: No Errors |
| Checkout view.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/views.py) | ![screenshot](documentation/modelcheckout.png) | Pass: No Errors |
| Checkout webhook_handler.py.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/webhook_handler.py) | ![screenshot](documentation/handlercheckout.png) | Pass: No Errors |
| Checkout webhooks.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/checkout/webhooks.py) | ![screenshot](documentation/webhook.png) | Pass: No Errors |
| Design apps.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/design/apps.py) | ![screenshot](documentation/appdesign.png) | Pass: No Errors |
| Design url.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/design/urls.py) | ![screenshot](documentation/urldesign.png) | Pass: No Errors |
| Design view.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/design/views.py) | ![screenshot](documentation/viewdesign.png) | Pass: No Errors |
| Designproduct admin.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/designproducts/admin.py) | ![screenshot](documentation/adminproduct.png) | Pass: No Errors |
| Designproduct apps.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/designproducts/apps.py) | ![screenshot](documentation/appprodesproducts.png) | Pass: No Errors |
| Designproduct forms.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/designproducts/forms.py) | ![screenshot](documentation/formsproduct.png) | Pass: No Errors |
| Designproduct models.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/designproducts/models.py) | ![screenshot](documentation/modelsproduct.png) | Pass: No Errors |
| Designproduct urls.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/designproducts/urls.py) | ![screenshot](documentation/urlproduct.png) | Pass: No Errors |
| designproduct widget.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/designproducts/widgets.py) | ![screenshot](documentation/widgetproduct.png) | Pass: No Errors |
| designproduct view.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/design/views.py) | ![screenshot](documentation/viewdesign.png) | Pass: No Errors |
| Profiles apps.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/profiles/apps.py) | ![screenshot](documentation/appprofile.png) | Pass: No Errors |
| Profiles forms.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/profiles/forms.py) | ![screenshot](documentation/formsprofile.png) | Pass: No Errors |
| Profiles models.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/profiles/models.py) | ![screenshot](documentation/modelprofile.png) | Pass: No Errors |
| Profiles urls.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/profiles/urls.py) | ![screenshot](documentation/urlsprofile.png) | Pass: No Errors |
| Profiles view.py | [PEP8 CI](https://github.com/Alena18/Coffeebeanstudio1809/blob/main/profiles/views.py) | ![screenshot](documentation/viewprofile.png) | Pass: No Errors |


## Browser Compatibilitys

I tested website using next browsers:

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/googlecoffee.png) | Works as expected |
| Firefox | ![screenshot](documentation/foxcoffee.png) | Works as expected |
| Edge | ![screenshot](documentation/edgecoffee.png) | Works as expected |
| Brave | ![screenshot](documentation/bravecoffee.png) | Works as expected |
| Opera | ![screenshot](documentation/operacoffee.png) | Minor differences |

## Responsiveness

I've tested my deployed project on multiple devices (mobile, tablet,  desktop) to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/galaxyeight.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/ipadmini.png) | Works as expected |
| Desktop | ![screenshot](documentation/desktop.png) | Works as expected |
| Ipad mini | ![screenshot](documentation/ipadminiland.png) | Works as expected |
| Surface Pro 7 | ![screenshot](documentation/surfaceproseven.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues and follow recommendation to make site more accessible.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot](documentation/desktoplighthousehome.png) | Few warnings |
| Home | Mobile | ![screenshot](documentation/moblighthouse.png) | Some minor warnings |
| Product view | Desktop | ![screenshot](documentation/desktopprodview.png) | Few warnings |
| Product view | Mobile | ![screenshot](documentation/mobileprodview.png) | Some minor warnings |
| Bag | Desktop | ![screenshot](documentation/desktopshopbag.png) | Few warnings |
| Bag | Mobile | ![screenshot](documentation/desktopshopbag.png) | Some minor warnings |

## Defensive Programming

I implement next defensive features:

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Product View page | Pass | |
| Product View Page | | | | |
| | Click on image | Redirection to Product Detail page | Pass | |
| Product Detail Page | | | | |
| | Add to bag  | Toast notice shows up | Pass | |
| | Click on cart | Redirection to Cart page  | Pass | |
| Cart Page | | | | |
| | Edit/Remove button | Check if edit/remove button works | Pass | |
| | Click to Checkout | Redirects to payment system | Pass | |
| | Click the Pay button | Redirects user to home page | Pass |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to be able to view a list of products, so that I can select some to purchase. | ![screenshot](documentation/listofprod.png) |
| As a new site user, I would like to view individual product details, so that I can identify the price, description, product rating. | ![screenshot](documentation/proddetail.png) |
| As a new site user, I would like to quickly identify deals, clearance items and special offers, so that I can take advantage of special savings on products user like to purchase. | ![screenshot](documentation/rate.png) |
| As a new site user, I would like to easily view the total of my purchases at any time , so that I can avoid spending too much. | ![screenshot](documentation/purchasetotal.png) |
| As a new site user, I would like to sort the list of available products, so that I can easily identify the best rated, best priced and categorically sorted products. | ![screenshot](documentation/sort.png) |
| As a returning site user, I would like to easily register for an account, so that I can have a personal account and be able to view my profile. | ![screenshot](documentation/register.png) |
| As a returning site user, I would like to easily login, so that I can access my personal account information. | ![screenshot](documentation/signincoffee.png) |
| As a returning site user, I would like to easily logout, so that I can access my personal account information. | ![screenshot](documentation/logoutcoffee.png) |
| As a returning site user, I would like to easily recover my password in case user forget it, so that I can recover access to my account. | ![screenshot](documentation/forgotpassw.png) |
| As a returning site user, I would like to receive an email confirmation after registering , so that I can verify that my account registration was successful. | ![screenshot](documentation/confirmsent.png) |
| As a returning site user, I would like to have a personalized user profile, so that I can view my personal order history and order confirmation and save my payment information. | ![screenshot](documentation/prof.png) |

## Bugs

| Bug | Status |
| --- | --- |
| [Heroku App](documents/apptail.png) | Closed |

| How it was fixed | Screenshot |
| --- | --- |
| Use Terminal |  [screenshot](documentation/bug.png) |
| Use Terminal |  [screenshot](documentation/debug.png) |
| Procfile |  [screenshot](documentation/procfile.png) |
| Solved |  [screenshot](documentation/profilesort.png) |
| Quantity button |  [screenshot](documentation/button.png) |
| Quantity button fix by Chris CodeInstitute |  [screenshot](documentation/buttonfix.png) |

## Unfixed Bugs

There are no remaining bugs that I am aware of.