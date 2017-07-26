from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Joãozinho', cpf='12345678901',
                    email='joaozinho@gmail.com', phone='84-555-5555')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'joaozinho@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Joãozinho',
            '12345678901',
            'joaozinho@gmail.com',
            '84-555-5555'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
