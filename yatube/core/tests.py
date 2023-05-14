from http import HTTPStatus

from django.test import Client, TestCase


class ViewTestClass(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

    # @unittest.skip('При добавлении хэндлера все страницы отдают 200 ОК')
    def test_error_page(self):
        response = ViewTestClass.client.get('/unexisting_page/')
        # Проверьте, что статус ответа сервера - 404
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        # Проверьте, что используется шаблон core/404.html
        self.assertTemplateUsed(response, 'core/404.html')
