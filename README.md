# McDogealds-Recipe-book
A recipe book app for python


## What is this?

McDogealds is an imaginary international fast food chain.

the owners of McDogealds, Landon flop (@ch1ck3n-byte) and Lord Technodoggo (@jondoglover) have finally released the recipes for their ground-breaking food!

**Developer view:**

A recipe app, made in django , python 3.9.

Visit `subs/urls.py` for all available urls.

### Dependencies:

Python 3.6+

Django 3

Markdown

```
pip install markdown
```

A computer

A command line

## How to use

McDogealds Recipe book requires **Python 3.6 or higher**. Download this repository onto your computer and open powershell or your command line into the repository directory.

Run

```
pip install django
```
check that you have a python version of 3.6 or more.
```
python -V
```

once you have the command line in the directory, run `python manage.py runserver`. open the url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser, and the recipes should be there.

## Online web version

McDogealds is now online! visit here: [https://mcdogealds-recipe-book-1.ch1ck3n.repl.co](https://mcdogealds-recipe-book-1.ch1ck3n.repl.co) **WARNING: it's outdated. not recommended.**

## Links

#### All recipes

  Visit `/things` for all recipes.

#### View recipe
  Visit `/things/{id}` where id is either 1, 2, 3, 4, and so on.
#### Add recipe
  Visit `/add` to add a recipe.

## Tips & tricks

#### Save current recipe list forever

  Visit `/tools/savecode`. copy the entire page.
  Go to `/subs/items.py` (in the code folder, not the web directory) and replace the entire file with the text you just copied.
