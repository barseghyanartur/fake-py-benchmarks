import cProfile
import os

import django_micro as app
from django.contrib import admin
from django.core.management.base import BaseCommand

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
SECRET_KEY = "1234"
STATIC_URL = "/static/"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}
CONTEXT_PROCESSORS = [
    "django.template.context_processors.request",
]
USE_TZ = True

app.configure(locals(), django_admin=True)

from factories.factory_boy_django_auth_minimal import (  # noqa
    UserFactory as FactoryBoyUserFactory,
)
from factories.fake_py_django_auth_minimal import (  # noqa
    UserFactory as FakePyUserFactory,
)


@app.command("run_django_auth_user_minimal_benchmark")
class RunDjangoAuthUserMinimalBenchmarkCommand(BaseCommand):
    def handle(self, *args, **options):
        print(
            f"Generating using factory_boy "
            f"({FactoryBoyUserFactory.__module__}."
            f"{FactoryBoyUserFactory.__name__}):"
        )
        cProfile.run("FactoryBoyUserFactory.create_batch(100)")
        print("*" * 20)

        print(
            f"Generating using fake.py "
            f"({FakePyUserFactory.__module__}."
            f"{FakePyUserFactory.__name__}):"
        )
        cProfile.run("FakePyUserFactory.create_batch(100)")
        print("*" * 20)

        print("-----" * 20)


app.route("admin/", admin.site.urls)

if __name__ == "__main__":
    application = app.run()
