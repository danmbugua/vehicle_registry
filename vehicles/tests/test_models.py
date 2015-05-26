from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Owner


class TestOwner(TestCase):
    def test_save(self):
        owner = Owner(
            id=1,
            id_number='12334556',
            first_name='Test',
            last_name='Test last_name'
        )
        owner.save()
        owner_refetched = Owner.objects.get(id=1)
        self.assertEquals(1, Owner.objects.count())
        self.assertEquals('12334556', owner_refetched.id_number)

    def test_valdate_id_number(self):
        owner = Owner(
            id=1,
            id_number='12345',
            first_name='Test',
            last_name='Test last_name'
        )
        with self.assertRaises(ValidationError):
            owner.save()
        self.assertEquals(0, Owner.objects.count())
