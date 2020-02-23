# flask-bookshelf

## Resources Used:

- Set up virtual env: https://docs.python-guide.org/dev/virtualenvs/
- Configure Flask + React App: https://itnext.io/a-template-for-creating-a-full-stack-web-application-with-flask-npm-webpack-and-reactjs-be2294b111bd
- postgresql for python: https://pypi.org/project/psycopg2/
- sqlalchemy & postgresql: https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
- weird error when trying to install psycopg2.. had to add LDFLAGS & CPPFLAGS to .zshrc
  https://github.com/pypa/pipenv/issues/3873

To run:

```
# run the Flask server
pipenv run python main.py

# run the React app on webpack
cd templates/static
npm run watch
```
