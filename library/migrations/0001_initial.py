
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.Author')),
            ],
            options={
                'ordering': ['book_name', 'author__last_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['genre_name'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('publisher_id', models.AutoField(primary_key=True, serialize=False)),
                ('publisher_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['publisher_name'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='library.Book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='library.Genre')),
            ],
            options={
                'ordering': ['genre__genre_name', 'book__book_name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.Publisher'),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('last_name', 'first_name')},
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('genre', 'book')},
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('book_name', 'author')},
        ),
    ]
