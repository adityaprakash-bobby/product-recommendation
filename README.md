# Improved Product Recommendation

This repo contains the source code for web application of the project "Improved Product Recommendation System" as a part of Dell Hack2Hire-2.0.

```bash
# Clone and setup the local dev server
git clone https://github.com/adityaprakash-bobby/ecomm
cd ecomm/
python3 -m venv virtualenv
. virtualenv/bin/activate
pip install -r requirements.txt

# Prep the backend, static files and the database
cd backend_ecommerce/
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Start the dev-server
python manage.py runserver
```
#### Further improvements:
- [ ] Revamp the UI
- [ ] Add a task manager for the backend
- [ ] Add custom analytics
- [ ] Implement adsense
- [ ] Add recommendation based on ads
