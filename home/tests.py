from django.test import TestCase

from home.models import *


# Create your tests here.
class UsersModelTest(TestCase):

    def setUp(self):
        self.user = Users.objects.create(
            name='Test User',
            email='test.user@example.com',
            status='active',
            avatar='path/to/avatar.jpg'
        )

    def test_slug_creation(self):
        self.assertEqual(self.user.slug, 'testuserexamplecom')

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.name)

class RoleModelTest(TestCase):

    def setUp(self):
        self.role = Role.objects.create(name='Admin')

    def test_string_representation(self):
        self.assertEqual(str(self.role), self.role.name)

class UserProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.user_profile), self.user.username)

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Technology')

    def test_slug_creation(self):
        self.assertEqual(self.category.slug, 'technology')

    def test_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)

class BlogPostModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Technology')
        self.blog_post = BlogPost.objects.create(
            title='First Post',
            description='This is the first post.',
            image='path/to/image.jpg',
            category=self.category
        )

    def test_slug_creation(self):
        self.assertEqual(self.blog_post.slug, 'first-post')

    def test_string_representation(self):
        self.assertEqual(str(self.blog_post), self.blog_post.title)

class PermissionModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Technology')
        self.permission = Permission.objects.create(category=self.category)

    def test_string_representation(self):
        self.assertEqual(str(self.permission), self.permission.category.name)


