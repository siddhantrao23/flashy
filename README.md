# flashy

A Flashcard Application made using Django

This project is hosted on heroku and can be found 
<a href="https://flashy-cards-app.herokuapp.com">here</a>

# Install

```
git clone https://github.com/siddhantrao23/flashy.git
cd flashy
pip3 install -r requirements.txt
```

# Run

`$ python3 manage.py runserver` to start up the server

Navigate to `localhost:8000/cards` to see the application in the browser

# Endpoints
- `/`: Homepage
- `/set_index/<set_id>`: Index page for a particular set
- `/new_set`: Form for creating a new set
- `/new_card/<int:set_id>`: Form for creating new Card in a set
- `/<int:set_id>/<int:card_id>`: Practice the flashcard set
- `/del_set`: Delete a flashcard set
- `/del_card/<int:set_id>`: Delete a card from a particular set

# TODO
- add error page
- delete card from particular set
