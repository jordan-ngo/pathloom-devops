# pathloom-devops

This repository contains two main files: permutations.py and test_perm.py. The permutations.py file 
includes a function for generating permutations of any data type. The test_perm.py file provides a 
suite of unit tests to validate the functionality of the permutations.py module.

The repository also includes a CI configuration file named python-ci.yml. Which automates the testing
and setup process using GitHub Actions. This CI pipeline runs automatically whenever there are pushes
to the repository, ensuring that new code is checked out and tested within a Python environment.

If you want to run the test yourself in an editor, running "python .\test_perm.py" will run all tests.
However, if you want to run individual unit tests, running "python .\test_perm.py TestPermutations.<test_name>"
will also work.
