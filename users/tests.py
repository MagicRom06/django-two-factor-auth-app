from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='test@test.com',
            password='test123456'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="super_test",
            email="supertest@test.com",
            password='supertest123456'
        )
        self.assertEqual(superuser.username, 'super_test')
        self.assertEqual(superuser.email, 'supertest@test.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
