import os

def test_pascal_2007_downloads():
  assert os.path.exists('./data/pascal_2007/VOCtrainval_06-Nov-2007.tar'), 'VOCtrainval_06-Nov-2007.tar not found.'
  assert os.path.exists('./data/pascal_2007/VOCtest_06-Nov-2007.tar'), 'VOCtest_06-Nov-2007.tar not found.'
  assert os.path.exists('./data/pascal_2007/VOCdevkit_08-Jun-2007.tar'), 'VOCdevkit_08-Jun-2007.tar not found.'
  print 'PASCAL VOC 2007 data files downloaded.'

def test_pascal_2007_extracts():
  assert os.path.exists('./data/pascal_2007/VOCdevkit'), 'VOCdevkit not found.'

  image_path = './data/pascal_2007/VOCdevkit/VOC2007/JPEGImages'
  num_images = len([f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))])
  assert num_images == 9963, 'Not all PASCAL VOC 2007 images downloaded and extracted'
  print 'PASCAL VOC 2007 data files extracted.'
