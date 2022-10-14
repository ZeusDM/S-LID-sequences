# Generating _S_-LID sequences, the quilt sequence, and the triangular quilt sequence.

The most important file in this folder is *slid.py*. It has the main functions that generate the next element of an _S_-LID sequence given all previous elements.
The terms of the sequences are saved in the folder *storage*.

You should not call the *slid.py* directly. Instead, use the command line to generate the next element of your favorite _S_-LID sequence, or repeatedly call *slid_powerset.py* or *slid_few_gaps.py* to generate the next elements of _S_-LID sequences for specific families of sets _S_; respectively, _S_ subset of {1, 2, 3, .., 10}, and _S_ of the form _[k] \ (k - T)_ for relatively small sets _T_.

The files *quilt.py* and *triangular_quilt.py* are very similar and they generate the Fibonacci quilt and triangular quilt sequences, respectively. To calculate the next term, call them directly.

