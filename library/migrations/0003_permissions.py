from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    book_permissions = permission_class.objects.filter(content_type__app_label='library',
                                                       content_type__model='book')

    author_permissions = permission_class.objects.filter(content_type__app_label='library',
                                                         content_type__model='author')

    genre_permissions = permission_class.objects.filter(content_type__app_label='library',
                                                        content_type__model='genre')

    section_permissions = permission_class.objects.filter(content_type__app_label='library',
                                                          content_type__model='section')

    member_permissions = permission_class.objects.filter(content_type__app_label='library',
                                                         content_type__model='member')

    publisher_permissions = permission_class.objects.filter(content_type__app_label='library',
                                                            content_type__model='publisher')

    perm_view_book = permission_class.objects.filter(content_type__app_label='library',
                                                     content_type__model='book',
                                                     codename='view_book')

    perm_view_author = permission_class.objects.filter(content_type__app_label='library',
                                                       content_type__model='author',
                                                       codename='view_author')

    perm_view_genre = permission_class.objects.filter(content_type__app_label='library',
                                                      content_type__model='genre',
                                                      codename='view_genre')

    perm_view_section = permission_class.objects.filter(content_type__app_label='library',
                                                        content_type__model='section',
                                                        codename='view_section')

    perm_view_member = permission_class.objects.filter(content_type__app_label='library',
                                                       content_type__model='member',
                                                       codename='view_member')

    perm_view_publisher = permission_class.objects.filter(content_type__app_label='library',
                                                          content_type__model='publisher',
                                                          codename='view_publisher')

    user_permissions = chain(perm_view_book,
                             perm_view_author,
                             perm_view_genre,
                             perm_view_section,
                             perm_view_member,
                             perm_view_publisher,
                             )

    librarian_permissions = chain(book_permissions,
                                  author_permissions,
                                  genre_permissions,
                                  section_permissions,
                                  member_permissions,
                                  publisher_permissions,
                                  )

    helper_permissions = chain(genre_permissions,
                              section_permissions,
                              publisher_permissions,
                              perm_view_member)

    my_groups_initialization_list = [
        {
            "name": "librarian",
            "permissions_list": librarian_permissions,
        },
        {
            "name": "helper",
            "permissions_list": helper_permissions,
        },
        {
            "name": "user",
            "permissions_list": user_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    Group = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = Group.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0002_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
