### photoapp

 Main Features
- Post a photo. --> Done
- Save photos as draft. --> Done
- Edit photo captions. --> Done
- Delete photos. --> Done
- List photos (all, my photos, my drafts) --> Done
- ASC/DESC Sort photos on publishing date --> Done
- Filter photos by user. --> Done
- Limit the uploaded photo size to a certain maximum dimensions and bytes. --> Done
- JWT authentication. --> Done
- Host it on Heroku --> Done
- Maintain a good git history. --> Tried 

 If time permits, add following features.
- Remove the dimension/size limit, and store the original photo, but serve only proportionally
- resized/cropped photos based on pre-defined dimensions. --> Done Partially
- Implement batch upload, edit, delete, publish API for photos.--> Done Bulk upload only
- Support #tags in captions, and filtering on the same. --> Not Done. 

## How to use

Clone this project:

```bash
$ git clone LOCATION_OF/project.bundle
```
CREATE AND ACTIVATE VIRTUAL ENV Python >= 3.6  (Handy tool : https://virtualenvwrapper.readthedocs.io/en/latest/)

Install dependencies:

```bash
$ pip install -r requirements.txt
```
Create local sqlite DB: 

```bash
$  echo "DATABASE_URL=sqlite:///db.sqlite3" > .env
```
Run DB Migrations

```bash
$  python manage.py migrate
```

Run test and view Coverage:

```bash
$  pytest
```

Run Server:

```bash
$  python manage.py runserver 
```
