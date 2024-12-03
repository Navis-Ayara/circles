<center><img src="src/assets/images/logo.svg" style="height:140;"><h1>Circles.</h1></center> 

## Social media for the minimalist
A simple social media web app build purely in Python.

# Tech stack
## Flet
The entire UI is written in Flet adhering to Python best practices for the best user interface possible with such a customizable framework. You can learn more about flet [here](https://flet.dev).

## Firebase
Whenever building any sort of backend with Python, it isn't uncommon for SQLAlchemy to take the stage. But for this particular project, Firebase was chosen due to its simplicity in creation and management of databases


### Miscleneous
Google Oauth 2.0 was used for user authentication so if you're going to run the project yourself, regestering Auth credentials is necessary. Just create a .env file in the same directory as the ```main.py``` file and place the clientID and clientSecret into variables named ```CLIENT_ID``` and ```CLIENT_SECRET```. If there's a future for this project, more authentication methods will be available

### Current progress
<input type="checkbox" disabled checked> Main UI

<input type="checkbox" disabled> Firebase Intergration

<input type="checkbox" disabled> Deployment

To run the app:
```
flet run [app_directory] -p 8550
```
<!-- TODO: The concept -->