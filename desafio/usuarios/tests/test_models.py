from django.contrib.auth.models import User
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from usuarios.models import UserProfile


class UserProfileModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )



#models


    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.create(user=self.user)
        self.assertIsInstance(user_profile, UserProfile)
        self.assertEqual(user_profile.user, self.user)
        self.assertIsNone(user_profile.phone_number)
        self.assertFalse(user_profile.profile_picture.name)  
        self.assertIsNone(user_profile.verification_code)
        self.assertIsNone(user_profile.reset_code)
        self.assertFalse(user_profile.is_verified)

    def test_user_profile_str(self):
        user_profile = UserProfile.objects.create(user=self.user)
        profile_str = str(user_profile)
        self.assertEqual(profile_str, self.user.username)

    def test_user_profile_phone_number(self):
        user_profile = UserProfile.objects.create(user=self.user, phone_number='123456789')
        self.assertEqual(user_profile.phone_number, '123456789')

    def test_user_profile_profile_picture(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        user_profile = UserProfile.objects.create(user=self.user, profile_picture=image)
        self.assertIsNotNone(user_profile.profile_picture)
        self.assertTrue(user_profile.profile_picture.name.startswith('profile_pictures/'))

    def test_user_profile_verification_code(self):
        user_profile = UserProfile.objects.create(user=self.user, verification_code='123456')
        self.assertEqual(user_profile.verification_code, '123456')

    def test_user_profile_reset_code(self):
        user_profile = UserProfile.objects.create(user=self.user, reset_code='654321')
        self.assertEqual(user_profile.reset_code, '654321')

    def test_user_profile_is_verified(self):
        user_profile = UserProfile.objects.create(user=self.user, is_verified=True)
        self.assertTrue(user_profile.is_verified)
