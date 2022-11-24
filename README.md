# Spellburn and Battlescars

A django web app to help run the RPG [Spellburn and Battlescars](https://xenio-in-a-bottle.itch.io/sab) by [Matheus Henrique Morais](https://xenio-in-a-bottle.itch.

All art by Emiel Boven. Support the artist at: [https://www.patreon.com/emielboven](https://www.patreon.com/emielboven)
    
## To run the projet locally

### Install the packages in a virtual environment
`pip install -r requirements.txt`


### set up environment variables
Create a `.env` file containing

>>>
SECRET_KEY=some_secret_key_of_your_own

ENVIRONMENT=development
>>>

### Set up the db
`python manage.py migrate`

### Run the local server
`python manage.py runserver`