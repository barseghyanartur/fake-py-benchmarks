from django.contrib.auth.models import User
from django.utils import timezone
from fake import FACTORY, FAKER, DjangoModelFactory, PreInit, PreSave

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2024 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("UserFactory",)


def set_password(user: User, password: str) -> None:
    user.set_password(password)


class UserFactory(DjangoModelFactory):
    """User factory.

    Usage example:

    .. code-block:: python

        # Create a user. Created user will automatically have his password
        # set to "test1234".
        user = UserFactory()

        # Create 5 users.
        users = UserFactory.create_batch(5)

        # Create a user with custom password
        user = UserFactory(
            password=PreSave(set_password, password="another-pass"),
        )
    """

    username = FACTORY.username()
    first_name = FACTORY.first_name()
    last_name = FACTORY.last_name()
    email = FACTORY.email()
    date_joined = FACTORY.date_time(tzinfo=timezone.get_current_timezone())
    last_login = FACTORY.date_time(tzinfo=timezone.get_current_timezone())
    is_superuser = False
    is_staff = False
    is_active = FACTORY.pybool()
    password = PreSave(set_password, password="test1234")

    class Meta:
        model = User
        get_or_create = ("username",)
