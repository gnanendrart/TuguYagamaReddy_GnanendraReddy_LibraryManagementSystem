from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from library.forms import BookForm, AuthorForm, SectionForm, GenreForm, PublisherForm, MemberForm
from library.models import Book, Author, Section, Genre, Publisher, Member
from library.utils import PageLinksMixin


class BookList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Book
    permission_required = 'library.view_book'


class BookDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'library.view_book'

    def get(self, request, pk):
        book = get_object_or_404(
            Book,
            pk=pk
        )
        section_list = book.sections.all()
        author = book.author
        publisher = book.publisher
        return render(
            request,
            'library/book_detail.html',
            {'book': book,
             'author': author,
             'publisher': publisher,
             'section_list': section_list}
        )


class BookCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = BookForm
    model = Book
    permission_required = 'library.add_book'


class BookUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = BookForm
    model = Book
    template_name = 'library/book_form_update.html'
    permission_required = 'library.change_book'


class BookDelete(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.delete_book'

    def get(self, request, pk):
        book = self.get_object(pk)
        sections = book.sections.all()
        if (sections.count()) > 0:
            return render(
                request,
                'library/book_refuse_delete.html',
                {'book':book,
                 'sections': sections}
            )
        else:
            return render(
                request,
                'library/book_confirm_delete.html',
                {'book': book}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Book,
            pk=pk
        )

    def post(self,request, pk):
        book = self.get_object(pk)
        book.delete()
        return redirect('library_book_list_urlpattern')


class AuthorList(LoginRequiredMixin,PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Author
    permission_required = 'library.view_author'


class AuthorDetail(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.view_author'

    def get(self, request, pk):
        author = get_object_or_404(
            Author,
            pk = pk
        )

        book_list = author.books.all()
        return render(
            request,
            'library/author_detail.html',
            {'author':author,
             'book_list': book_list,
             }
        )


class AuthorCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = AuthorForm
    model = Author
    permission_required = 'library.add_author'


class AuthorUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = AuthorForm
    model = Author
    template_name = 'library/author_form_update.html'
    permission_required = 'library.change_author'


class AuthorDelete(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.delete_author'

    def get(self, request, pk):
        author = self.get_object(pk)
        books = author.books.all()
        if books.count() > 0:
            return render(
                request,
                'library/author_refuse_delete.html',
                {'author':author,
                 'books':books
                 }
            )
        else:
            return render(
                request,
                'library/author_confirm_delete.html',
                {'author': author}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Author,
            pk=pk
        )

    def post(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return redirect('library_author_list_urlpattern')


class MemberList(LoginRequiredMixin,PermissionRequiredMixin,PageLinksMixin, ListView):
    paginate_by = 10
    model = Member
    permission_required = 'library.view_member'


class MemberDetail(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.view_member'

    def get(self, request, pk):
        member = get_object_or_404(
            Member,
            pk = pk
          )
        return render(
            request,
            'library/member_detail.html',
            {'member': member
             }
        )


class MemberCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = MemberForm
    model = Member
    permission_required = 'library.add_member'


class MemberUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = MemberForm
    model = Member
    template_name = 'library/member_form_update.html'
    permission_required = 'library.change_member'


class MemberDelete(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.delete_member'

    def get(self, request, pk):
        member = self.get_object(pk)
        return render(request,
                      'library/member_confirm_delete.html',
                      {'member': member})

    def get_object(self, pk):
        return get_object_or_404(
            Member,
            pk=pk
        )

    def post(self,request, pk):
        member= self.get_object(pk)
        member.delete()
        return redirect('library_member_list_urlpattern')


class SectionList(LoginRequiredMixin,PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Section
    permission_required = 'library.view_section'


class SectionDetail(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.view_section'

    def get(self, request, pk):
        section = get_object_or_404(
            Section,
            pk=pk
        )
        genre = section.genre
        book = section.book
        return render(
            request,
            'library/section_detail.html',
            {'section':section,
             'genre': genre,
             'book': book,
             }
        )


class SectionCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = SectionForm
    model = Section
    permission_required = 'library.add_section'


class SectionUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = SectionForm
    model = Section
    template_name = 'library/section_form_update.html'
    permission_required = 'library.update_section'


class SectionDelete(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Section
    success_url = reverse_lazy('library_section_list_urlpattern')
    permission_required = 'library.delete_section'


class GenreList(LoginRequiredMixin,PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Genre
    permission_required = 'library.view_genre'


class GenreDetail(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.view_genre'

    def get(self, request, pk):
        genre = get_object_or_404(
            Genre,
            pk = pk
        )

        section_list = genre.sections.all()
        return render(
            request,
            'library/genre_detail.html',
            {'genre':genre,
             'section_list': section_list}
        )


class GenreCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = GenreForm
    model = Genre
    permission_required = 'library.add_genre'


class GenreUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = GenreForm
    model = Genre
    template_name = 'library/genre_form_update.html'
    permission_required = 'library.change_genre'


class GenreDelete(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.delete_genre'

    def get(self, request, pk):
        genre = self.get_object(pk)
        sections = genre.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'library/genre_refuse_delete.html',
                {'genre':genre,
                 'sections':sections
                 }
            )
        else:
            return render(
                request,
                'library/genre_confirm_delete.html',
                {'genre': genre}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Book,
            pk=pk
        )

    def post(self,request, pk):
        book = self.get_object(pk)
        book.delete()
        return redirect('library_genre_list_urlpattern')


class PublisherList(LoginRequiredMixin,PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Publisher
    permission_required = 'library.view_publisher'


class PublisherDetail(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.view_publisher'

    def get(self, request, pk):
        publisher = get_object_or_404(
            Publisher,
            pk = pk
        )

        book_list = publisher.books.all()
        return render(
            request,
            'library/publisher_detail.html',
            {'publisher':publisher,
             'book_list':book_list}
        )


class PublisherCreate(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    form_class = PublisherForm
    model = Publisher
    permission_required = 'library.add_publisher'


class PublisherUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    form_class = PublisherForm
    model = Publisher
    template_name = 'library/publisher_form_update.html'
    permission_required = 'library.change_publisher'


class PublisherDelete(LoginRequiredMixin,PermissionRequiredMixin, View):
    permission_required = 'library.delete_publisher'

    def get(self, request, pk):
        publisher = self.get_object(pk)
        books = publisher.books.all()
        if books.count()  > 0:
            return render(
                request,
                'library/publisher_refuse_delete.html',
                {'publisher':publisher,
                 'books': books
                 }
            )
        else:
            return render(
                request,
                'library/publisher_confirm_delete.html',
                {'publisher': publisher}
            )

    def get_object(self, pk):
        return get_object_or_404(
            Publisher,
            pk=pk
        )

    def post(self,request, pk):
        publisher = self.get_object(pk)
        publisher.delete()
        return redirect('library_publisher_list_urlpattern')
