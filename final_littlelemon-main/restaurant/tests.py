from django.test import TestCase
from .models import Booking, Menu
from datetime import date

class BookingTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            first_name="Test",
            reservation_date=date.today(),
            reservation_slot=10
        )
        self.assertEqual(booking.first_name, "Test")

    def test_unique_booking(self):
        Booking.objects.create(
            first_name="A",
            reservation_date=date.today(),
            reservation_slot=10
        )
        with self.assertRaises(Exception):
            Booking.objects.create(
                first_name="B",
                reservation_date=date.today(),
                reservation_slot=10
            )


class MenuTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(
            name="Pizza",
            price=100,
            menu_item_description="Test"
        )
        self.assertEqual(menu.name, "Pizza")