# django-fixture-decorator

django-fixture-decorator provides an easy-to-use decorator for Django test cases, enabling automatic fixture loading for individual test methods. This allows greater flexibility by loading fixtures on a per-test basis, rather than for the entire test case as with setUp and tearDown. Reduce boilerplate and streamline your test setup by handling fixture management directly within the test method itself.

## Usage

To use the `django-fixture-decorator` in your Django tests, simply import the decorator and apply it to your test methods. This will automatically load the specified fixture for each individual test, allowing for more granular control over your test setup.

### Example

Here’s a basic example of how to use the decorator in a Django test case:

```python
from django.test import TestCase
from django_fixture_decorator import load_fixture

class MyModelTests(TestCase):

    @load_fixture('my_fixture.json')
    def test_my_model_functionality(self):
        # Your test logic here
        my_model_instance = MyModel.objects.get(pk=1)
        self.assertEqual(my_model_instance.field_name, 'expected_value')

    @load_fixture('another_fixture.json')
    def test_another_functionality(self):
        # Another test logic with a different fixture
        another_model_instance = AnotherModel.objects.get(pk=1)
        self.assertTrue(another_model_instance.is_active)
