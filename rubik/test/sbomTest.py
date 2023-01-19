'''
Created on Jan 19, 2023

@author: Colby
'''
import unittest
import app

class SbomTest(unittest.TestCase):


    def test_sbom_100_ShouldReturnAuthorName(self):
        myName = 'cjd0057'
        result = app._getAuthor('../../')
        resultingAuthorName = result['author']
        self.assertEqual(resultingAuthorName, myName)
