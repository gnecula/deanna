
import motifs
import unittest

class TestMotifs(unittest.TestCase):

  def test_motif_1(self):
    self.assertEqual(motifs.split_motifs("abi"), [("ab", 0)])
    self.assertEqual(motifs.split_motifs("aib"), [("a", 0), ("b", 2)])

  def test_motif_2(self):
    self.assertEqual(motifs.split_motifs_2(""), [])
    self.assertEqual(motifs.split_motifs_2("abi"), [("ab", 0)])
    self.assertEqual(motifs.split_motifs_2("aib"), [("a", 0), ("b", 2)])
    self.assertEqual(motifs.split_motifs_2("i0aib"), [("a", 2), ("b", 4)])
    self.assertEqual(motifs.split_motifs_2("i0aiib00"), [("a", 2), ("b", 5)])