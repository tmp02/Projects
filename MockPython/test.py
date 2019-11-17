from unittest import TestCase
from unittest.mock import patch, Mock
import request

MockResponse = [
            {
                'id':1,
                'title':'Test Title',
            },
            {
                'id':2,
                'title':'Second Title',
            }
        ]

class TestBlog(TestCase):
    @patch('request.Blog.posts', return_value= MockResponse)
    def test_blog_posts(self,MockPosts):
        blog = request.Blog('Meu Blog!')
        response = blog.posts()
        MockPosts.assert_called_once_with()
        self.assertEqual(blog.showContent(response), 'Blog Name: Meu Blog!\nTitle: Test Title')

