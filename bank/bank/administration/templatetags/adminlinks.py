import importlib
from importlib import import_module, util
from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag()
def adminlinks():
    menus: list[dict] = []

    for installed_app in settings.INSTALLED_APPS:
        index: int = 0
        split: list[str] = installed_app.split('.')

        for element in split:
            if element == 'apps':
                del split[index:split.__len__()]
                break

            index += 1

        if util.find_spec('.'.join(split) + ".admin") is not None:
            importlib.invalidate_caches()

            try:
                module = import_module('.'.join(split) + ".admin")

                if hasattr(module, "AdministrationLinks"):
                    instance = getattr(module, "AdministrationLinks")()
                    menus.append(getattr(instance, "get")())
            except LookupError:
                pass

    return menus
