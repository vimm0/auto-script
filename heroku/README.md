`heroku login`

### requirements.txt
```
dj-database-url==0.4.2
gunicorn==19.7.1
psycopg2==2.7.1
whitenoise==3.3.0
```

### runtime.txt
```
python-3.7.0

```
### wsgi.py
```
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "merolekha.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

```

### settings.py
```
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CORS_ORIGIN_ALLOW_ALL = True

```
#### Procfile
```
web: gunicorn merolekha.wsgi --log-file -

```
`Note: commit changes`


# For static file
- `npm install express serve-static --save`
- `npm run build`
```
const express = require('express')
const serveStatic = require('serve-static')
const path = require('path')
// create the express app
const app = express()
// create middleware to handle the serving the app
app.use("/", serveStatic ( path.join (__dirname, '/dist') ) )
// Catch all routes and redirect to the index file
app.get('*', function (req, res) {
    res.sendFile(__dirname + '/dist/index.html')
})
// Create default port to serve the app on
const port = process.env.PORT || 5000
app.listen(port)
// Log to feedback that this is actually running
console.log('Server started on port ' + port)
```

run 

- `node server.js
`

### Procfile
- `web: node server.js` 

- build latest before push
- remove /dist/ form ignore file
## Heroku commands
- `heroku create <app-name>`
- Test locally, `heroku local web`
- To disable collectstatic command, `heroku config:set DISABLE_COLLECTSTATIC=1`
- `git push heroku master`
- if postgres, `heroku addons:create heroku-postgresql:hobby-dev`
- if branch, `git push heroku testbranch:master`
