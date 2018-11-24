# FactoryProducts
DJango API to retrieve products from different factories given by an X-KEY-API in headers.

## Explanation
This approach sets a dynamic serializer depending on the factory set in the X-KEY-API, this is used in order to resctrict sending the whole general product information set for all the factories to every user.

Of course, the method of the key to distinguish between manufacturers is not the best approach. In order to have a better structurization and function of the app an engine for every factory would be the best solution. If we can bind users to factories it could be easier to set up a custom authorization to ensure users only access to their own factories. This approach would have the inconvenience of either having to double login, one for the platform itself and one for the factory the user has access to, or the one login to the main platform and an automated authorization process by the factory per se.

## Installation

1. Download the project.
2. Inside the project file execute `pip install` to install all project's dependencies.
3. Run `python manage.py makemigrations` and `python manage.py migrate` to perform proper migrations.
4. Run `python manage.py runserver`.
