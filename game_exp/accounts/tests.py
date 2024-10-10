from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import GameExpUser, Profile, Language, Token, EmailNotification

class TestAccountsModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testcase_user1', 
            password='testcase1', 
            email='testcase1@gmail.com'
        )

        Language.objects.create(lang_name='English')

        refresh_token = RefreshToken.for_user(self.user)
        expired_at = timezone.now() + timedelta(days=30)
        self.token = Token.objects.create(refresh_token=str(refresh_token), expired_at=expired_at)
        
        self.game_exp_user = GameExpUser.objects.create(
            user=self.user,
            token=self.token,
            is_player=True,
            is_developer=False,
            is_apply_news=True,
            is_accepting_terms=True,
        )
        self.game_exp_user.save()
        
    
    def test_game_exp_user_creation(self):
        self.assertIsNotNone(self.game_exp_user)
        self.assertIsNotNone(self.game_exp_user.token)
        self.assertEqual(self.game_exp_user.user.username, 'testcase_user1')
        self.assertEqual(self.game_exp_user.user.email, 'testcase1@gmail.com')
        self.assertTrue(self.game_exp_user.is_player)

    def test_profile_creation(self):
        profile = Profile.objects.get(user=self.game_exp_user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.display_name, 'testcase_user1')
        self.assertEqual(profile.profile_url, 'http://127.0.0.1/users/profile/testcase_user1')

    def test_email_settings_created(self):
        settings = EmailNotification.objects.get(user=self.game_exp_user)
        self.assertIsNotNone(settings)
        self.assertEqual(settings.is_never_send, False)
