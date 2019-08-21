
```
python-pygraphviz
pkg-config 

$ pip install django-extensions pygraphviz

```

```
INSTALLED_APPS = [ 
                   ...
                   'django_extensions',
]
#ALERT while copying: inverted comma in medium is different
```

```
#To group all the application and output into PNG file
$ python manage.py graph_models -a -g -o imagefile_name.png
#Include only some applications
$ python manage.py graph_models app1 app2 -o app1_app2.png
#Include only some specific models
$ python manage.py graph_models -a -I Foo,Bar -o foo_bar.png
#OR exclude certain models 
$ python manage.py graph_models -a X Foo,Bar -o no_foo_bar.png
```

```
if problem in graph try
$ pip install pydot pyparsing==1.5.7 #use this specific version

```

```
$ python manage.py graph_models -a > dotfile.dot
$ python manage.py graph_models app1 app2 > fire_me.dot
$ python manage.py graph_models -a -I Foo,Bar > something.dot
$ python manage.py graph_models -a X Foo,Bar > nofoobar.dot

```

```
$ python manage.py graph_models -a -o myapp_models.png
$ python manage.py show_urls
$ python manage.py validate_templates
$ python manage.py shell_plus
$ python manage.py runserver_plus

```

https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16
