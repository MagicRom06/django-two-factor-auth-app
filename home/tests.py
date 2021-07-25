from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class LoginPageTest(TestCase):

    def test_login_page_status_code(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login')
        self.assertTemplateUsed(response, 'account/login.html')


class SignupPageTest(TestCase):

    def test_signup_page_status_code(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'signup')
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
                username='test',
                password='test12345'
        )
        self.assertEqual(
            get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].username, new_user.username)


class HomePageTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
                username='test',
                password='test12345'
        )

    def test_home_page_status_code(self):
        self.client.login(
            username=self.user.username,
            password=self.user.password
        )
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
