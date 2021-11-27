import unittest

from webscraper.dl import dl_image_from_url, dl_video_from_url


class TestDownloadImage(unittest.TestCase):

    def test_dl_img_no_except(self):
        excep = False
        try:
            dl_image_from_url('https://images.pexels.com/photos/10305718/pexels-photo-10305718.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260')
        except Exception as e:
            excep = True

        self.assertFalse(excep)

class TestDownloadVideo(unittest.TestCase):

    def test_dl_vi_no_except(self):
        excep = False
        try:
            dl_video_from_url(
                'https://ia902504.us.archive.org/13/items/SampleVideo_908/Bear.mp4')
        except Exception as e:
            excep = True

        self.assertFalse(excep)
