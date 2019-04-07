# A RestAPI implemented in Django-rest-framework for a thumbnail generator App!

## Requirements

Python (3.4, 3.5, 3.6, 3.7)
Django (1.11, 2.0, 2.1)

## API Features
* Endpoint - localhost:8000/profile/ # where post request is to be made
* If using postman, use form-data and key:'photo', value:<actual image file>
* Provide endpoint to accept images in PNG and JPG format
* Return a processed image in 3 different resolutions - small, medium and large
* REST feature and complete possiblitiy to 
    - add more endpoints
    - scale if needed in future
    - fast response
    - connect with front end like React


## Implementation Details:

* Images:
    - Images are less than 5Mb of size
    - We assume that user uses the api for quick resizing

* Receiving data:
    - For our purposes we can assume this API will be used by a single provider, so no need to keep track of which provider is sending the
    message.

## Specification for data sent by external providers

The external providers will send the data in any possible format but we are handling only JPG and PNG formats.

## Message Types

* NewEvent:
A complete new sporting event is being created. Once the event is created successfully
the only field that will updated is the selection odds.

* UpdateOdds:
There is an update for the odds field (all the other fields remain unchanged)

## Installation

Install using pip...

pip install -r requirements.txt

That's it, we're done!

## How to run?

If running on local machine do
```python
python manage.py runserver
./manage.py runserver
```

You can now open the API in your browser at http://127.0.0.1:8000/, and view your new API.
For this exercise we are not using authentication. So all users have full CRUD access.

If you don't use the database provided on your local machine you need to do the
migrations and create a super user.

python manage.py createsuperuser

Access admin panel at http://127.0.0.1:8000/admin/
From the admin panel you can do more operations like add, create and delete models,
users, do grouping, etc.

You can also interact with the API using command line tools such as curl. For example, to list the match endpoint:


Example

Let's take a look at a quick example of using REST framework to build a simple model-backed API.


Startup up a new project like so...
```python
pip install django
pip install djangorestframework
django-admin startproject example .
./manage.py migrate
./manage.py createsuperuser
```
Now edit the `example/urls.py` module in your project:
```python
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'url', 'name', 'startTime')
```

```python


# ViewSets define the view behavior.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
```

```python

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'match', MatchViewSet)

```
```python
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

```
We'd also like to configure a couple of settings for our API.

Add the following to your settings.py module:
```python
INSTALLED_APPS = (
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
```
Documentation & Support

Full documentation for the project is available at https://www.django-rest-framework.org/.
