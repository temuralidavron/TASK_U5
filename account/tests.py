from django.contrib.auth import get_user_model
from django.test import TestCase

from account.serializers import UserRegisterSerializer

user = get_user_model()


class UserTest(TestCase):
    def setUp(self):
        self.validate_data = {
            'username': 'test',
            "email": 'test@gmail.com',  # to‘g‘rilandi
            'password': '1995'
        }

    def test_user_serializers_is_valid(self):
        serializers = UserRegisterSerializer(data=self.validate_data)
        self.assertTrue(serializers.is_valid())
        self.assertEqual(serializers.errors, {})

    def test_user_create_serializers(self):
        serializers = UserRegisterSerializer(data=self.validate_data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        self.assertEqual(user.email, 'test@gmail.com')  # to‘g‘rilandi
        self.assertEqual(user.username, 'test')
        self.assertTrue(user.check_password('1995'))  # to‘g‘rilandi
        print(user.password)
