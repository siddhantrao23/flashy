# flashy

A Flashcard Application made using Django

# Install

```
git clone ps://github.com/siddhantrao23/flashy.git
cd flashy
pip3 install -r requirements.txt
```

# Run

`$ python3 manage.py runserver` to start up the server

Navigate to `localhost:8000/cards` to see the application in the browser

# Endpoints
- `/`: Homepage
- `/set_index/<set_id>`: Index page for a particular Set
- `/new_set`: Form for creating a new Set
- `/new_card/<int:set_id>`: Form for creating new Card in a set
- `/<int:set_id>/<int:card_id>`: Practice the flashcard set
