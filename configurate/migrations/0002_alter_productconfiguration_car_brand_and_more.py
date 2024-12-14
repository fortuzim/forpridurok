# Generated by Django 5.1.1 on 2024-10-05 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productconfiguration',
            name='car_brand',
            field=models.CharField(blank=True, choices=[('Wiberz', 'Wiberz auto'), ('Abarth', 'Abarth'), ('Acura', 'Acura'), ('Alfa Romeo', 'Alfa Romeo'), ('Aston Martin', 'Aston Martin'), ('Aixam', 'Aixam'), ('Audi', 'Audi'), ('Bentley', 'Bentley'), ('BMW', 'BMW'), ('Cadillac', 'Cadillac'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Citroën', 'Citroën'), ('Cupra', 'Cupra'), ('Dacia', 'Dacia'), ('Daewoo', 'Daewoo'), ('Dodge', 'Dodge'), ('DS', 'DS'), ('Ferrari', 'Ferrari'), ('Fisker', 'Fisker'), ('Ford', 'Ford'), ('FSO Polonez', 'FSO Polonez'), ('GMC', 'GMC'), ('Honda', 'Honda'), ('Hummer', 'Hummer'), ('Hyundai', 'Hyundai'), ('Infinity', 'Infinity'), ('Isuzu', 'Isuzu'), ('Iveco', 'Iveco'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Lamborghini', 'Lamborghini'), ('Lancia', 'Lancia'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Lincoln', 'Lincoln'), ('Lotus', 'Lotus'), ('Lublin', 'Lublin'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mercedes-Benz', 'Mercedes-Benz'), ('MG', 'MG'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Porsche', 'Porsche'), ('Renault', 'Renault'), ('Rolls Royce', 'Rolls Royce'), ('Rover', 'Rover'), ('SaaB', 'SaaB'), ('Scion', 'Scion'), ('Seat', 'Seat'), ('Skoda', 'Skoda'), ('Smart', 'Smart'), ('SsangYong', 'SsangYong'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productconfiguration',
            name='carpet_color',
            field=models.CharField(blank=True, choices=[('Czerwony', 'Czerwony'), ('Szary', 'Szary'), ('Ciemny niebieski', 'Ciemny niebieski'), ('Jasny niebieski', 'Jasny niebieski'), ('Beżowy', 'Beżowy'), ('Jasny Beżowy', 'Jasny Beżowy'), ('Brązowy', 'Brązowy'), ('Jasny Szary', 'Jasny Szary'), ('Czarny', 'Czarny')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productconfiguration',
            name='color',
            field=models.CharField(blank=True, choices=[('Czerwony', 'Czerwony'), ('Szary', 'Szary'), ('Ciemny niebieski', 'Ciemny niebieski'), ('Jasny niebieski', 'Jasny niebieski'), ('Beżowy', 'Beżowy'), ('Jasny Beżowy', 'Jasny Beżowy'), ('Brązowy', 'Brązowy'), ('Jasny Szary', 'Jasny Szary'), ('Czarny', 'Czarny')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productconfiguration',
            name='complete_set',
            field=models.CharField(choices=[('Wybierz komplet', 'Wybierz komplet'), ('ETC Zestaw 2D (przód, tył, tunel) - 390 PLN', 'ETC Zestaw 2D (przód, tył, tunel) - 390 PLN'), ('ETC Zestaw przód 2D - 250 PLN', 'ETC Zestaw przód 2D - 250 PLN'), ('ETC Zestaw tył 2D - 200 PLN', 'ETC Zestaw tył 2D - 200 PLN'), ('Nie potrzebuję dywaników tylko matę', 'Nie potrzebuję dywaników tylko matę')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productconfiguration',
            name='mat',
            field=models.CharField(blank=True, choices=[('Nie potrzebuję maty', 'Nie potrzebuję maty'), ('Mata do bagażnika - 300 PLN', 'Mata do bagażnika - 300 PLN')], max_length=100),
        ),
        migrations.AlterField(
            model_name='productconfiguration',
            name='production_year',
            field=models.CharField(blank=True, choices=[('Wybierz rok produkcji', 'Wybierz rok produkcji'), ('2024', '2024'), ('2023', '2023'), ('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'), ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'), ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970')], max_length=21),
        ),
    ]