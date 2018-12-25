### Important django third party apps for django admin
```bash
# ADMIN
https://github.com/jsocol/django-adminplus *

# CUSTOMIZATION

https://github.com/s-block/django-nested-inline
https://github.com/Soaa-/django-nested-inlines
https://github.com/theatlantic/django-nested-admin

https://github.com/modlinltd/django-advanced-filters
https://github.com/jonasundderwolf/django-image-cropping
https://github.com/areski/django-admin-tools-stats
https://github.com/stephenmcd/django-forms-builder
https://github.com/silentsokolov/django-admin-rangefilter
https://github.com/daniyalzade/django_reverse_admin
https://github.com/samluescher/django-form-designer
https://github.com/alesdotio/django-admin-shortcuts
https://github.com/clintecker/django-chunks
https://github.com/jphalip/django-treemenus
https://github.com/lazybird/django-solo
https://github.com/chrisspen/django-chroniker *
https://github.com/ebertti/django-admin-easy
https://github.com/praekelt/django-object-tools
https://github.com/burke-software/django-mass-edit
https://github.com/runekaagaard/django-admin-flexselect
https://github.com/burke-software/django-report-builder
https://github.com/django-request/django-request
https://github.com/fgmacedo/django-export-action
https://github.com/omji/django-tabbed-admin
https://github.com/mishbahr/django-modeladmin-reorder
https://github.com/purelabs/django-bulk-admin
https://github.com/cdrx/django-admin-menu
https://github.com/Bearle/django_mail_admin
https://spapas.github.io/2015/01/21/django-model-auditing/
https://github.com/django/django-localflavor
django-extra-views
Django-extensions
https://github.com/scaphilo/koalixcrm
https://django-bmf.org/
django-form-utils

# PERFORMANCE
https://github.com/ionelmc/django-redisboard

# ADMIN REST: 
https://github.com/erdem/django-admino

# PRACTICAL
https://github.com/QingdaoU/OnlineJudge
https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
https://code.djangoproject.com/wiki/NewformsHOWTO
```

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
