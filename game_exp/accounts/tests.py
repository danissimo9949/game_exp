from django.test import TestCase
from django.contrib.auth.models import User
from .models import GameExpUser, Profile, Language

class TestAccountsModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testcase_user1', 
            password='testcase1', 
            email='testcase1@gmail.com'
        )

        Language.objects.create(lang_name='English')
        
        self.game_exp_user = GameExpUser.objects.create(
            user=self.user,
            is_player=True,
            is_developer=False,
            is_apply_news=True,
            is_accepting_terms=True,
        )
        self.game_exp_user.save()
    
    def test_game_exp_user_creation(self):
        self.assertIsNotNone(self.game_exp_user)
        self.assertEqual(self.game_exp_user.user.username, 'testcase_user1')
        self.assertEqual(self.game_exp_user.user.email, 'testcase1@gmail.com')
        self.assertTrue(self.game_exp_user.is_player)

    def test_profile_creation(self):
        profile = Profile.objects.get(user=self.game_exp_user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.display_name, 'testcase_user1')
        self.assertEqual(profile.profile_name, 'testcase_user1')
