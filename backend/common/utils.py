from pathlib import Path

from django.conf import settings


def get_all_apps() -> list[str]:
    apps_dir = Path(settings.ROOT_DIR)
    apps = []
    for item in apps_dir.iterdir():
        if item.is_dir() and (item / '__init__.py').exists() and item.name != 'config':
            apps.append(item.name)

    return sorted(apps)
