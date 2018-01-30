from setuptools import setup

setup(name='dissertation',
      version='0.2.47',
      description='Third-year dissertation project in predictive analytics for new product development',
      # url='http://github.com/',
      author='Josh Hills',
      author_email='J.Hills@ncl.ac.uk',
      license='MIT',
      packages=['api', 'shared', 'review', 'client', 'results', 'store', 'update'],
      zip_safe=False)
