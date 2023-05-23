from django.test import TestCase

# Create your tests here.

# Path: gallery\tests.py

# Write for views.py

class GalleryViewTest(TestCase):
    def test_gallery_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'gallery.html')
    

class ImageDetailViewTest(TestCase):
    # Test for image 1 and image 2
    def test_image_detail_view(self):
        response = self.client.get('/image/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name: 1')
        
        response = self.client.get('/image/2/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Name: 2')

        # Get text from response


