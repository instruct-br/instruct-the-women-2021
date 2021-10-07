from rest_framework.test import APITestCase


class OpenTests(APITestCase):
    def test_titan_project(self):
        django_version = "2.2.24"
        titan = {
            "name": "titan",
            "packages": [
                {"name": "django-rest-swagger"},
                {"name": "Django", "version": django_version},
                {"name": "psycopg2-binary", "version": "2.9.1"},
            ],
        }
        response = self.client.post("/api/projects/", titan, format="json")
        self.assertEqual(response.status_code, 201)

        response_data = response.json()
        packages = response_data["packages"]

        django = next(pkg for pkg in packages if pkg["name"] == "Django")
        self.assertEqual(django["version"], django_version)

        drs = next(pkg for pkg in packages if pkg["name"] == "django-rest-swagger")
        self.assertEqual(drs["version"], "2.2.0")

    def test_unknown_package(self):
        mh_data = {
            "name": "machine-head",
            "packages": [
                {"name": "keras"},
                {"name": "matplotlib"},
                {"name": "pypypypypypypypypypypypypy"},
            ],
        }
        response = self.client.post("/api/projects/", mh_data, format="json")
        self.assertEqual(response.status_code, 400)

        response_data = response.json()
        self.assertDictEqual(
            response_data, {"error": "One or more packages doesn't exist"}
        )
