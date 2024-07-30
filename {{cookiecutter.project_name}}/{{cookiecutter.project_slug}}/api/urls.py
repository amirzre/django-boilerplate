from django.urls import include, path

urlpatterns = [
    path("auth/", include(("{{cookiecutter.project_slug}}.authentication.urls", "authentication"))),
    path("users/", include(("{{cookiecutter.project_slug}}.users.urls", "users"))),
    path("errors/", include(("{{cookiecutter.project_slug}}.errors.urls", "errors"))),
    path("files/", include(("{{cookiecutter.project_slug}}.files.urls", "files"))),
    path(
        "google-oauth2/", include(("{{cookiecutter.project_slug}}.blog_examples.google_login_server_flow.urls", "google-oauth2"))
    ),
]
