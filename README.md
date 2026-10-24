# Apostol Calculus – An Applied and Visual Study Project

This repository is an applied and computational companion to the following books:

Tom M. Apostol, *Calculus, Volume 1* and *Calculus, Volume 2*, Second Edition,
John Wiley & Sons, New York.

Publisher's official page:
https://www.wiley.com/en-us/Calculus%2C+Volume+1%2C+2nd+Edition-p-9780471000051

This project was started on January 15, 2026 by Muhammed Ikbal Yilmaz. It is a living project: new chapters, solved
exercises and visualizations are added as the work progresses.

---

## About the Book

Apostol's books are known for their careful, axiomatic development of calculus and for emphasizing ideas and
structure rather than treating the subject as a collection of computational tricks.

The first volume develops one-variable calculus together with the necessary foundations of linear algebra. The second
volume continues with multivariable calculus, differential equations, linear analysis, and probability.

---

## Purpose of This Repository

The purpose of this repository is not to reproduce the text of the books. Instead, it aims to provide a working
environment where the material can be explored using computation and visualization.

In this repository:

- Concepts are examined through numerical experiments,
- Geometric ideas are supported by plots and figures,
- Calculations are checked using symbolic computation,
- Selected exercises are implemented and tested in code.

The notebooks are written primarily for personal study, but they are kept public in the hope that they may also be
useful to others working through the same material.

---

## Copyright and Use of the Source

This repository does not contain the text of the books.

- No definitions, theorems, or explanations are copied from the source; where they are needed, they are restated
  briefly in my own words.
- References are given by chapter, section, exercise and page number.
- All code, explanations, and figures in this repository are original.

The books are the work of Tom M. Apostol, and their copyright belongs to the author and the publisher. Anyone who wants
to study them should obtain the books from the publisher. This project is not intended to replace the books, but to
accompany them.

---

## Contents

Section numbers and pages refer to the second edition.

| Volume 1 | Sections | Pages | Notebook |
|---|---|---|---|
| Introduction, Part 1. Historical Introduction | I 1.1–I 1.6 | 1–10 | [historical-introduction](volume-1/00-introduction/part-1-historical-introduction/historical-introduction.ipynb) |
| Introduction, Part 2. Some Basic Concepts of the Theory of Sets | I 2.1–I 2.5 | 11–15 | [some-basic-concepts-of-the-theory-of-sets](volume-1/00-introduction/part-2-theory-of-sets/some-basic-concepts-of-the-theory-of-sets.ipynb) |

Each notebook is also saved as an HTML file in the same folder, and its figures are in the `figures/` folder next to
it.

Still to come, in the order of the books:

- **Volume 1.** Introduction, Part 3. A Set of Axioms for the Real-Number System; Part 4. Mathematical Induction,
  Summation Notation, and Related Topics; 1. The Concepts of Integral Calculus; 2. Some Applications of Integration;
  3. Continuous Functions; 4. Differential Calculus; 5. The Relation between Integration and Differentiation; 6. The
  Logarithm, the Exponential, and the Inverse Trigonometric Functions; 7. Polynomial Approximations to Functions;
  8. Introduction to Differential Equations; 9. Complex Numbers; 10. Sequences, Infinite Series, Improper Integrals;
  11. Sequences and Series of Functions; 12. Vector Algebra; 13. Applications of Vector Algebra to Analytic Geometry;
  14. Calculus of Vector-Valued Functions; 15. Linear Spaces; 16. Linear Transformations and Matrices.
- **Volume 2.** Part 1. Linear Analysis: 1. Linear Spaces; 2. Linear Transformations and Matrices; 3. Determinants;
  4. Eigenvalues and Eigenvectors; 5. Eigenvalues of Operators Acting on Euclidean Spaces; 6. Linear Differential
  Equations; 7. Systems of Differential Equations. Part 2. Nonlinear Analysis: 8. Differential Calculus of Scalar and
  Vector Fields; 9. Applications of the Differential Calculus; 10. Line Integrals; 11. Multiple Integrals; 12. Surface
  Integrals. Part 3. Special Topics: 13. Set Functions and Elementary Probability; 14. Calculus of Probabilities;
  15. Introduction to Numerical Analysis.

---

## Project Structure

```
apostol/        reusable helper code: the figure style (style.py), the sums of the method of exhaustion (sums.py),
                operations on finite sets (sets.py)
volume-1/       one folder per chapter (00-introduction for the Introduction) and one subfolder per part, each with
                its notebook (.ipynb), the same notebook as HTML, and a figures/ folder
tests/          automated tests that check the helper code against independent computations
fonts/          Latin Modern Roman, the typeface of the figures (GUST Font License)
```

A `volume-2/` folder is added when the work on the second volume starts.

---

## How to Run

```
pip install -r requirements.txt
jupyter lab                 # open a notebook and run all cells; the sliders need a running kernel
pytest                      # run the tests from the repository root
```

All figures follow one style: Latin Modern Roman, black and deep blue, labelled ticks at both ends of every value
axis, no minor ticks. Each figure is checked when it is saved; a figure whose axis does not end at a labelled tick, or
in which two pieces of text overlap, is not written.

---

## Tools

- Python
- NumPy
- SymPy
- Matplotlib
- Jupyter Lab and ipywidgets
- PyTest

---

## How to Cite the Books

If you want to cite Apostol's books in LaTeX / BibTeX, you can use the following entries:

```bibtex
@book{ApostolCalculus1,
  author    = {Tom M. Apostol},
  title     = {Calculus, Volume 1: One-Variable Calculus, with an Introduction to Linear Algebra},
  edition   = {Second},
  publisher = {John Wiley \& Sons},
  address   = {New York},
  year      = {1967},
  isbn      = {0-471-00005-1}
}

@book{ApostolCalculus2,
  author    = {Tom M. Apostol},
  title     = {Calculus, Volume 2: Multi-Variable Calculus and Linear Algebra with Applications to Differential
               Equations and Probability},
  edition   = {Second},
  publisher = {John Wiley \& Sons},
  address   = {New York},
  year      = {1969},
  isbn      = {0-471-00007-8}
}
```

---

## Author and License

Muhammed Ikbal Yilmaz (myucanlar@gmail.com)

The code, notes and figures of this repository are released under the MIT License (see [LICENSE](LICENSE)). The
license does not cover the books.
