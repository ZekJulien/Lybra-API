$env:PYTHONPATH="apps"
$env:DJANGO_SETTINGS_MODULE="core.settings.dev"
pytest apps/users/tests
