from setuptools import setup


setup(name='QCGym', version='v0.0.4-alpha', packages=['QCGym'], license='MIT',
      description='A Collection of Gym environments used in Quantum control',
      author='Vedant Meshra', author_email='meshravedant@gmail.com',
      url='https://github.com/CodeMesh15/QRLgym',
      keywords=['Quantum', 'Control', 'Gym', 'RL'],
      # And any other dependencies foo needs,
      install_requires=['gym==0.18.0', 'numpy==1.19.5', 'scipy==1.6.1'],
      classifiers=[
          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Development Status :: 3 - Alpha',
          # Define that your audience are scientists
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Physics',
          # Specify which python versions that you want to support
          'Programming Language :: Python :: 3.8',
],
)
