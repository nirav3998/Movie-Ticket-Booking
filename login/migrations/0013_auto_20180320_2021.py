# Generated by Django 2.0.2 on 2018-03-20 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_remove_cinema_bdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='cinema_id',
        ),
        migrations.RemoveField(
            model_name='show',
            name='cinema_id',
        ),
        migrations.RemoveField(
            model_name='show',
            name='movie_id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='show_id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='ticketoffer',
            name='offer_id',
        ),
        migrations.RemoveField(
            model_name='ticketoffer',
            name='ticket_id',
        ),
        migrations.DeleteModel(
            name='Cinema',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Offers',
        ),
        migrations.DeleteModel(
            name='Show',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='TicketOffer',
        ),
    ]
