def split_motifs(labels: str):
  """Split the labels strings into motifs.

  A motif is a sequence of consecutive letters in "labels",
  not including "i" or "0".

  Returns:
    list of pairs, with the motif substring, and the index in labels where
    it starts.
  """
  motifs = []
  motif_start_index = -1  # The index in labels of the first syllable in the motif
  for i, label in enumerate(labels):
    if label == "i" or label == "0":
      if motif_start_index >= 0:  # we are inside a motif
        motifs.append((labels[motif_start_index:i], motif_start_index))
        motif_start_index = -1  # mark that we are not in a motif anymore
      else:
        # we are not in a motif, keep going (multiple consecutive separators)
        continue
    else:
      # a syllable
      if motif_start_index >= 0:
        # already inside a motif
        continue
      else:
        # We start a motif
        motif_start_index = i

  return motifs
