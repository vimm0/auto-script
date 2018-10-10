- sudo pacman -S python-pip cairo pango gdk-pixbuf2 libffi pkg-config
- pip install -r requirements.txt
- export SECRET_KEY='<mysecretkey>'
- sudo -u postgres psql
- create user,password and database as saleor 
- And also ALTER USER root WITH SUPERUSER;

- python manage.py migrate

# Frontend
- npm install
- npm run build-assets
- npm run build-emails

