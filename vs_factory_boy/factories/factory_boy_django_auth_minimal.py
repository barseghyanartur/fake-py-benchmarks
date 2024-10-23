from django.contrib.auth.models import User
from django.utils import timezone
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2024 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("UserFactory",)


class UserFactory(DjangoModelFactory):
    """User factory.

    Usage example:

    .. code-block:: python

        # Create a user. Created user will automatically have his password
        # set to "test1234" and will be added to the group "Test group".
        user = UserFactory()

        # Create 5 users.
        users = UserFactory.create_batch(5)

        # Create a user with custom password
        user = UserFactory(
            password=PreSave(set_password, password="another-pass"),
        )
    """

    username = Faker("user_name")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    date_joined = Faker(
        "date_time_between",
        start_date="-30m",
        end_date="-20m",
        tzinfo=timezone.get_current_timezone(),
    )
    last_login = Faker(
        "date_time_between",
        start_date="-30m",
        end_date="-20m",
        tzinfo=timezone.get_current_timezone(),
    )
    is_superuser = False
    is_staff = False
    is_active = Faker("pybool")

    class Meta:
        model = User
        django_get_or_create = ("username",)

    @post_generation
    def set_password(self, created, extracted, **kwargs):
        """Set user password only for newly created instances."""
        if created:
            if not self.password or not self.has_usable_password():
                self.set_password("test1234")
                self.save(update_fields=["password"])
