import os

def test_pascal_2007_downloads():
  assert os.path.exists('./data/pascal_2007/VOCtrainval_06-Nov-2007.tar'), 'VOCtrainval_06-Nov-2007.tar not found.'
  assert os.path.exists('./data/pascal_2007/VOCtest_06-Nov-2007.tar'), 'VOCtest_06-Nov-2007.tar not found.'
  assert os.path.exists('./data/pascal_2007/VOCdevkit_08-Jun-2007.tar'), 'VOCdevkit_08-Jun-2007.tar not found.'
  print 'PASCAL VOC 2007 data files downloaded.'

def test_pascal_2007_extracts():
  assert os.path.exists('./data/pascal_2007/VOCdevkit'), 'VOCdevkit not found.'

  #num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
  print 'PASCAL VOC 2007 data files extracted.'
