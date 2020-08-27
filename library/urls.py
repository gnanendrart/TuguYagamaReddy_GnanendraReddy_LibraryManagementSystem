from django.urls import path

from library import views
from .views import (AuthorList, AuthorDetail, SectionList, SectionDetail, BookList, BookDetail,
                    GenreList, GenreDetail, PublisherList, PublisherDetail, AuthorCreate, SectionCreate,
                    BookCreate, GenreCreate, PublisherCreate, AuthorUpdate, AuthorDelete, SectionUpdate, SectionDelete,
                    BookUpdate, BookDelete, GenreUpdate, GenreDelete, PublisherUpdate, PublisherDelete, MemberList,
                    MemberDetail, MemberCreate, MemberUpdate, MemberDelete)

urlpatterns = [
    path('author/',
         AuthorList.as_view(),
         name='library_author_list_urlpattern'),

    path('author/<int:pk>/',
         AuthorDetail.as_view(),
         name='library_author_detail_urlpattern'),

    path('author/create/',
         AuthorCreate.as_view(),
         name='library_author_create_urlpattern'),

    path('author/<int:pk>/update/',
         AuthorUpdate.as_view(),
         name='library_author_update_urlpattern'),

    path('author/<int:pk>/delete/',
         AuthorDelete.as_view(),
         name='library_author_delete_urlpattern'),

    path('section/',
         SectionList.as_view(),
         name='library_section_list_urlpattern'),

    path('section/<int:pk>/',
         SectionDetail.as_view(),
         name='library_section_detail_urlpattern'),

    path('section/create/',
         SectionCreate.as_view(),
         name='library_section_create_urlpattern'),

    path('section/<int:pk>/update/',
         SectionUpdate.as_view(),
         name='library_section_update_urlpattern'),

    path('section/<int:pk>/delete/',
         SectionDelete.as_view(),
         name='library_section_delete_urlpattern'),

    path('book/',
         BookList.as_view(),
         name='library_book_list_urlpattern'),

    path('book/<int:pk>/',
         BookDetail.as_view(),
         name='library_book_detail_urlpattern'),

    path('book/create/',
         BookCreate.as_view(),
         name='library_book_create_urlpattern'),

    path('book/<int:pk>/update/',
         BookUpdate.as_view(),
         name='library_book_update_urlpattern'),

    path('book/<int:pk>/delete/',
         BookDelete.as_view(),
         name='library_book_delete_urlpattern'),

    path('member/',
         MemberList.as_view(),
         name='library_member_list_urlpattern'),

    path('member/<int:pk>/',
         MemberDetail.as_view(),
         name='library_member_detail_urlpattern'),

    path('member/create/',
         MemberCreate.as_view(),
         name='library_member_create_urlpattern'),

    path('member/<int:pk>/update/',
         MemberUpdate.as_view(),
         name='library_member_update_urlpattern'),

    path('member/<int:pk>/delete/',
         MemberDelete.as_view(),
         name='library_member_delete_urlpattern'),

    path('genre/',
         GenreList.as_view(),
         name='library_genre_list_urlpattern'),

    path('genre/<int:pk>/',
         GenreDetail.as_view(),
         name='library_genre_detail_urlpattern'),

    path('genre/create/',
         GenreCreate.as_view(),
         name='library_genre_create_urlpattern'),

    path('genre/<int:pk>/update/',
         GenreUpdate.as_view(),
         name='library_genre_update_urlpattern'),

    path('genre/<int:pk>/delete/',
         GenreDelete.as_view(),
         name='library_genre_delete_urlpattern'),

    path('publisher/',
         PublisherList.as_view(),
         name='library_publisher_list_urlpattern'),

    path('publisher/<int:pk>/',
         PublisherDetail.as_view(),
         name='library_publisher_detail_urlpattern'),

    path('publisher/create/',
         PublisherCreate.as_view(),
         name='library_publisher_create_urlpattern'),

    path('publisher/<int:pk>/update/',
         PublisherUpdate.as_view(),
         name='library_publisher_update_urlpattern'),

    path('publisher/<int:pk>/delete/',
         PublisherDelete.as_view(),
         name='library_publisher_delete_urlpattern'),
]