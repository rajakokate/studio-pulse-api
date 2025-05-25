# Optional: Save data if needed
rm -rf studiopulse_api/migrations
find . -name "__pycache__" -exec rm -rf {} +

# Clear DB (only if you don't mind wiping it)
rm db.sqlite3

# Re-initialize migrations
python manage.py makemigrations studiopulse_api
python manage.py migrate

