### Django tenant

- Migrate `./manage.py migrate_schemas --shared  # migrate database to public schema`
- Open Shell `./manage.py shell`
```
from apps.customer.models import Client 
   ...: # create your public tenant 
   ...: tenant = Client(domain_url='my-domain.com', # don't add your port or www here! on a local server you'll want to use localhost here 
   ...:                 schema_name='website', # change to app name or suitable schema name otherwise tenant doesnot migrate
   ...:                 name='Schemas Inc.', # organization name
   ...:                 paid_until='2016-12-05', 
   ...:                 on_trial=False) # for later use: billing purpose
   ...: tenant.save()      
   create client now
```
- create superuser`./manage.py createsuperuser --schema=website`



## django-tenant-schemas
```
# DUMP DATA
./manage.py tenant_command dumpdata --schema="schema-name" app_name.model_name --indent 4 > fixtures/dump.json
# LOAD DATA
./manage.py tenant_command loaddata --schema=schema_name dump.json 
# with out foreignkey and natural key
python manage.py tenant_command dumpdata --natural-foreign --natural-primary --schema="schema_name" app.modelname
./manage.py tenant_command dumpdata --schema="gvn" app.modelname --natural-foreign --natural-primary --indent 4 > dump.json
```
