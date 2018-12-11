### Auto Fixture Django:

Django Package: `django-autofixture`

For models involving ForeignKey

``` 
  from apps.payroll.models import Designation, Employee

  In [2]: from autofixture import AutoFixture
  
  In [3]: fixture = AutoFixture(Designation, generate_fk=True)
  
  In [4]: fixture.create(50)
```

### TEST

Integration with coverage.py

- first install coverage.py in system
- `coverage run --source='.' manage.py test myapp`
- `coverage report
