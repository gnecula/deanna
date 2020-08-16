
import motifs
import unittest

class TestMotifs(unittest.TestCase):

  def test_motif_1(self):
    self.assertEqual(motifs.split_motifs("abi"), [("ab", 0)])