from django.core.exceptions import ValidationError
from django.test import TestCase
from VetClinic.accounts.validators import UsernameValidator


class UsernameValidatorTest(TestCase):

    def setUp(self):
        self.validator = UsernameValidator()

    def test_valid_usernames(self):
        valid_usernames = [
            "user.name",
            "username123",
            "user_name",
            "user-name",
            "username.123",
        ]
        for username in valid_usernames:
            try:
                self.validator(username)
            except ValidationError as e:
                self.fail(f"Username '{username}' raised ValidationError: {e}")

    def test_invalid_usernames(self):
        invalid_usernames = [
            "user@name",
            "user name",
            "user!",
            "user#name",
            "user name 123",
            "username/123",
            "user-name!",
        ]
        for username in invalid_usernames:
            with self.assertRaises(ValidationError):
                self.validator(username)

    def test_error_message(self):
        invalid_username = "user@name"
        with self.assertRaises(ValidationError) as cm:
            self.validator(invalid_username)
        error_message = str(cm.exception).strip("'[]'")
        self.assertEqual(error_message, self.validator.message)
