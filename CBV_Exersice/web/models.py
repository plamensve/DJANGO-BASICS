from django.db import models


class TruckRoots(models.Model):
    TRUCK_NUMBER_MAX_LENGTH = 8
    TANK_NUMBER_MAX_LENGTH = 8
    CLIENT_NAME_MAX_LENGTH = 20
    DRIVER_NAME_MAX_LENGTH = 20

    client = models.CharField(
        max_length=CLIENT_NAME_MAX_LENGTH,
        null=False,
        blank=False
    )

    date_of_the_course = models.DateField()

    truck_number = models.CharField(
        max_length=TRUCK_NUMBER_MAX_LENGTH,
        null=False,
        blank=False
    )

    tank_number = models.CharField(
        max_length=TANK_NUMBER_MAX_LENGTH,
        null=False,
        blank=False
    )

    driver_name = models.CharField(
        max_length=DRIVER_NAME_MAX_LENGTH,
        null=False,
        blank=False
    )