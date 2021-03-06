from django.test import TestCase
from django.contrib.auth import get_user_model

from .. import models


def sample_user(email='marcelodimb@gmail.com', password='123456'):
    """Create sample user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Model tests."""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful."""
        email = 'marcelodimb@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized."""
        email = 'marcelodimb@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_create_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'marcelodimb@gmail.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation."""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
