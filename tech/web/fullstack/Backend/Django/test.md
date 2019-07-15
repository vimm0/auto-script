Integration with coverage.py

- first install coverage.py in system
- `coverage run --source='.' manage.py test myapp`
- `coverage report`

Abstract Model for Test
```
from django.db import connection
from django.db.models.base import ModelBase
from django.db.utils import OperationalError
from django.test import TestCase


class AbstractModelMixinTestCase(TestCase):
    """
    Base class for tests of model mixins/abstract models.
    To use, subclass and specify the mixin class variable.
    A model using the mixin will be made available in self.model
    """

@classmethod
def setUpTestData(cls):
    # Create a dummy model which extends the mixin. A RuntimeWarning will
    # occur if the model is registered twice
    if not hasattr(cls, 'model'):
        cls.model = ModelBase(
            '__TestModel__' +
            cls.mixin.__name__, (cls.mixin,),
            {'__module__': cls.mixin.__module__}
        )

    # Create the schema for our test model. If the table already exists,
    # will pass
    try:
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(cls.model)
        super(AbstractModelMixinTestCase, cls).setUpClass()
    except OperationalError:
        pass

@classmethod
def tearDownClass(self):
    # Delete the schema for the test model. If no table, will pass
    try:
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(self.model)
        super(AbstractModelMixinTestCase, self).tearDownClass()
    except OperationalError:
        pass
```
```
class MyModelTestCase(AbstractModelMixinTestCase):
    """Test abstract model."""
    mixin = MyModel

    def setUp(self):
        self.model.objects.create(pk=1)

    def test_a_thing(self):
        mod = self.model.objects.get(pk=1)
```
