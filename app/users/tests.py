from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from transactions.models import Transaction

'''
Base tests for users and transactions
'''


# TODO: Add more tests
class TestUser(TestCase):
    first_name_1 = 'Petr'
    last_name_1 = 'Ivanov'
    email_1 = 'ivanov@test.ru'

    first_name_2 = 'Anna'
    last_name_2 = 'Pavlova'
    email_2 = 'pavlova@test.ru'

    client = Client()

    def setUp(self):
        self.first_user = CustomUser.objects.create_user(email=self.email_1,
                                                         password='12345678',
                                                         first_name=self.first_name_1,
                                                         last_name=self.last_name_1)

    def test_user_create(self):
        url = reverse('users')
        response = self.client.post(url, data={'first_name': self.first_name_2,
                                               'last_name': self.last_name_2,
                                               'email': self.email_2})

        self.assertEqual(response.status_code, 201)

    def test_same_user_create(self):
        url = reverse('users')

        response = self.client.post(url, data={'first_name': self.first_name_1,
                                               'last_name': self.last_name_1,
                                               'email': self.email_1})

        self.assertEqual(response.status_code, 400)

    def test_get_user(self):
        url = reverse('user', kwargs={'pk': self.first_user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# TODO: Add more tests
class TestTransaction(TestCase):
    first_name = 'Petr'
    last_name = 'Ivanov'
    email = 'ivanov@test.ru'

    client = Client()

    def setUp(self):
        self.user = CustomUser.objects.create_user(email=self.email,
                                                   password='12345678',
                                                   first_name=self.first_name,
                                                   last_name=self.last_name)
        self.first_transaction = Transaction.objects.create(user=self.user, date='2021-01-01', amount=1000)

    def test_transaction_create(self):
        url = reverse('transactions')
        response = self.client.post(url, data={'user': self.user.pk, 'date': '2021-01-01', 'amount': 1000})
        self.assertEqual(response.status_code, 201)

    def test_get_transaction(self):
        url = reverse('transaction', kwargs={'pk': self.first_transaction.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
