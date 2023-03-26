# Notification API
A notification app for sending notifications using different channels

## Backend Tech Stack
1. Python
2. Django
3. DRF

## Frontend Tech Stack
1. React

## Backend Setup:
1. Install all deps using
```bash
pip install -r requirements.txt
```
2. Run migrations using
```bash
python manage.py migrate
```
3. Create root user using
```bash
python manage.py createsuperuser
```
4. Run application using
```bash
python manage.py runserver
```

## Frontend Setup:
1. Install all deps using
```
npm install
```
2. Run application using
```
npm start
```

## How to add data
1. Visit django admin on `localhost:8000/admin`
2. Log into admin portal and add channels, categories and mock users.

## API endpoints
1. GET /logs/
Will provide all logs available
2. GET /logs/string
Will provide a string representation of logs
3. POST /add/
For adding new messages
required fields : **message** , **category**


## How to extend notification channels
1. Add channel name in Channel model choices in main/models.py
2. Inherit from NotificationDispatcher class in main/notifications.py and override send_notification() method
the application will automatically detect new channel and send notifications.


## Note:
application is already loaded with sample data in db.sqlite3
### Users data
#### There are 3 users
1. Test user 1 |
receives email, push and sms notifications
2. Test user 2 |
only receives email notifications
3. Test user 3 |
only receives SMS notifications

**All users are subscribed to all message types**
