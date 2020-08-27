from django import forms
from library.models import Book, Section, Author, Genre, Publisher, Member
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'date_of_birth' : DateInput(),
            'date_of_death' : DateInput()
        }

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_date_of_birth(self):
        return self.cleaned_data['date_of_birth']

    def clean_date_of_death(self):
        data = self.cleaned_data['date_of_death']

        if data is None:
            return data
        if data < self.clean_date_of_birth():
            raise ValidationError(_('Invalid date - Date of Death should be after Date of Birth'))
        else:
            return data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_book_name(self):
        return self.cleaned_data['book_name'].strip()

    def clean_language(self):
        return self.cleaned_data['language'].strip()


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
            return self.cleaned_data['last_name'].strip()


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    def clean_genre_name(self):
        return self.cleaned_data['genre_name'].strip()


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

    def clean_publisher_name(self):
        return self.cleaned_data['publisher_name'].strip()