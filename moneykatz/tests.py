from django.test import TestCase

# Create your tests here.
from moneykatz.models import Category
from django.core.urlresolvers import reverse


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        """
        If no categories exist, an appropriate message should be displayed
        :return:
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['categories'], [])
        # look in cats.html
        self.assertContains(response, "Where the hell are the categories?")


class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        """
            Should result True for categories whose views are >= 0
        """
        cat = Category(name='test', views=-5, likes=0)
        cat.save()
        self.assertEqual(cat.views >= 0, True)

    def test_slug_line_creatiion(self):
        """
            slug_line_creation checks to make sure that when we add a category an appropriate slug line is created
            i.e. "Random Category String" -> "random-category-string"
        """

        cat = Category(name='Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')
