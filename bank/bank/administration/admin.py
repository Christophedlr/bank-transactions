from abc import ABC
from django.contrib import admin


class AbstractAdministrationLinks(ABC):
    """
    Managing administration menus
    """

    menu: dict = {}

    def add_menu(self, name: str):
        """
        Adding new menu for administration links.

        :param name: A string name of menu.
        """
        self.menu[name] = []

    def add_link(self, menu_name: str, name: str, url_resolver: str):
        """
        Adding new link in selected menu.

        :param menu_name: A string name of menu
        :param name: A string name of link
        :param url_resolver: A string name of url defined in urls.py
        """
        if menu_name in self.menu:
            self.menu[menu_name].append({
                'name': name,
                'url': url_resolver,
            })

    def get(self):
        """
        Get all administration menu.

        :return: A dict of menu
        """
        return self.menu
