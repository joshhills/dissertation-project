from setuptools import setup

setup(name='dissertation',
      version='0.2.72',
      description='Third-year dissertation project in predictive analytics for new product development',
      # url='https://github.com/joshhills/dissertation-project/',
      author='Josh Hills',
      author_email='J.Hills@ncl.ac.uk',
      license='MIT',
      packages=['api', 'shared', 'review', 'client', 'store', 'update', 'usage'],
      zip_safe=False)