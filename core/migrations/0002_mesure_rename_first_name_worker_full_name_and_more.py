# Generated by Django 4.0 on 2021-12-30 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largeur_epaule', models.FloatField(blank=True, null=True)),
                ('epaule_coude', models.FloatField(blank=True, null=True)),
                ('epaule_poignet', models.FloatField(blank=True, null=True)),
                ('nuque_poitrine', models.FloatField(blank=True, null=True)),
                ('nuque_bas_blouse', models.FloatField(blank=True, null=True)),
                ('tour_biceps', models.FloatField(blank=True, null=True)),
                ('tour_poignet', models.FloatField(blank=True, null=True)),
                ('tour_cou', models.FloatField(blank=True, null=True)),
                ('dessus_proitrine', models.FloatField(blank=True, null=True)),
                ('poitrine', models.FloatField(blank=True, null=True)),
                ('taile', models.FloatField(blank=True, null=True)),
                ('hanche_3', models.FloatField(blank=True, null=True)),
                ('hanche_7', models.FloatField(blank=True, null=True)),
                ('hanche_9', models.FloatField(blank=True, null=True)),
                ('longueur_devant', models.FloatField(blank=True, null=True)),
                ('longueur_dos', models.FloatField(blank=True, null=True)),
                ('carrure_devant', models.FloatField(blank=True, null=True)),
                ('carrure_dos', models.FloatField(blank=True, null=True)),
                ('epaule_a_l_autre', models.FloatField(blank=True, null=True)),
                ('tour_fourche', models.FloatField(blank=True, null=True)),
                ('hauteur_fourche', models.FloatField(blank=True, null=True)),
                ('tour_cuisse', models.FloatField(blank=True, null=True)),
                ('laterale_jambe', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='worker',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='location',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name',
        ),
        migrations.AddField(
            model_name='client',
            name='tranche_d_age',
            field=models.CharField(choices=[('En', 'Enfant'), ('Ado', 'Adolescent'), ('Adulte', 'Adulte')], default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modele',
            name='add_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='echantillon',
            field=models.ImageField(default=1, upload_to='images/echantillons'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='result',
            field=models.ImageField(default=1, upload_to='images/articles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='worker_cv'),
        ),
        migrations.AddField(
            model_name='worker',
            name='since',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='manager',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=255),
        ),
        migrations.AlterField(
            model_name='modele',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/modeles'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('C', 'En Conception'), ('T', 'Termine'), ('M', 'Attente de materiel')], max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='worker',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='salary',
            field=models.CharField(blank=True, default='NA', max_length=255),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='logo',
            field=models.ImageField(blank=True, default='images/logo.png', null=True, upload_to='images/logos/'),
        ),
        migrations.AddField(
            model_name='client',
            name='mesure',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.mesure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='mesure',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.mesure'),
            preserve_default=False,
        ),
    ]
