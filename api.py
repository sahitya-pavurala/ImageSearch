from clarifai.rest import ClarifaiApp, Image
from config_reader import CLARIFAI_KEY, CLARIFAI_SECRET
from hashlib import md5

def chunks(iterator, size):
    """
    Split the image url list to n lists of size 128
    :param iterator: List
    :param size: Integer
    :return: List[List]
    """
    for index in range(0, len(iterator), size):
        yield iterator[index:index + size]

def get_clarifai_app_object(urls):
    """
    Initialize indexing of images and return clarifai api object
    :param urls: List
    :return: ClarifaiApp
    """
    c_app = ClarifaiApp(
        CLARIFAI_KEY,
        CLARIFAI_SECRET)
    for arrays in chunks(urls, 128):
        try:
            c_app.inputs.bulk_create_images(
                [Image(url=url, image_id=md5(url).hexdigest()) for url in arrays])
        except:
            print "Trying to index duplicate images"
    return c_app
