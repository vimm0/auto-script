# Create Graph django-model
`sudo pacman -S graphviz`

`pip install pydot`

`pip install pygraphviz`

`./manage.py graph_models -a -g -o my_project_visualized.png`

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

# Reference

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html#selecting-a-library)
- https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16
