#### Run the App
```
flask --app app run --debug
```

#### Initialise the database
```
flask db init
```

#### Create Database Migration
```
flask db migrate -m "users table"
```

#### Apply migrations
```
flask db upgrade
```