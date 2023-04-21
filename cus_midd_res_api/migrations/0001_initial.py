# Generated by Django 4.2 on 2023-04-21 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(blank=True, max_length=105, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('number_of_openings', models.IntegerField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('requirement', models.CharField(choices=[('python', 'Python Developer'), ('react', 'React Developer')], default='python', max_length=12)),
                ('perks_and_benefits', models.TextField(blank=True, null=True)),
                ('skills_required', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('resume', models.FileField(upload_to='media')),
                ('expected_salary', models.IntegerField(default=0)),
                ('experience_type', models.CharField(choices=[('fresher', 'Fresher'), ('experience', 'Experience')], default='fresher', max_length=30)),
                ('skills', models.CharField(max_length=255)),
                ('current_salary', models.IntegerField(blank=True, null=True)),
                ('notice_period', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('apply_date', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cus_midd_res_api.candidatedetail')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cus_midd_res_api.job')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('college_name', models.CharField(max_length=255)),
                ('degree', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=255)),
                ('passout_year', models.DateField(blank=True, null=True)),
                ('job_apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cus_midd_res_api.jobapply')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CandidateExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cus_midd_res_api.jobapply')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
