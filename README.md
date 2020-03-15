# flask-bookshelf

## Resources Used:

- Set up virtual env: https://docs.python-guide.org/dev/virtualenvs/
- Configure Flask + React App: https://itnext.io/a-template-for-creating-a-full-stack-web-application-with-flask-npm-webpack-and-reactjs-be2294b111bd
- postgresql for python: https://pypi.org/project/psycopg2/
- sqlalchemy & postgresql: https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
- weird error when trying to install psycopg2.. had to add LDFLAGS & CPPFLAGS to .zshrc
  https://github.com/pypa/pipenv/issues/3873
- [Building a Simple Web App With Bottle, SQLAlchemy, and the Twitter API](https://realpython.com/building-a-simple-web-app-with-bottle-sqlalchemy-twitter-api/) & their [repo](https://github.com/pybites/pytip)
- [Goodreads API documentation](https://www.goodreads.com/api/index)
- [Filter by date/time with SQLalchemy](https://stackoverflow.com/questions/51451768/sqlalchemy-querying-with-datetime-columns-to-filter-by-month-day-year/51468737)
- [Example Glitch project](https://veil-look.glitch.me/posts/2019-books/#how-to-books)
- [Python read CSV](https://docs.python.org/3/library/csv.html)
- [Open Library Covers API](https://openlibrary.org/dev/docs/api/covers)
- [Mega Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Docker Project Walkthrough](https://circleci.com/docs/2.0/project-walkthrough/)
- [CircleCI Demo Python Flask](https://github.com/CircleCI-Public/circleci-demo-python-flask)
- [Deploy Python Flask app with Heroku](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0) 


To install dependencies:
1. Start the virtual environment
  `python3 -m venv venv`
2. Install
  `pipenv install -r requirements.txt`

Export Goodreads Reviews:
Go to https://www.goodreads.com/review/import
Export to CSV
Save it as `goodreads_library_export.csv` in the root of this project.

To run:

First, add environment variables to the `SAMPLE.env` file and rename it to just `.env`

```
# run the Flask server
pipenv run python main.py

# run the React app on webpack
cd templates/static
npm run watch
```

## Questions to Research later

- [ ] Why does Python require all these `__init__.py` files?
