### Auto Fixture Django:
Django Package: `django-autofixture`

For models involving ForeignKey

``` 
  from apps.payroll.models import Designation, Employee

  In [2]: from autofixture import AutoFixture
  
  In [3]: fixture = AutoFixture(Designation, generate_fk=True)
  
  In [4]: fixture.create(50)
```