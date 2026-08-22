# Mathematical references

This bibliography supports the literate source and executable mathematical essays in `tests/classical/` and `tests/research/`. Individual tests should still cite the specific entries they rely on and, when practical, include chapter/section/equation locators close to the argument.

The repository is public-domain software; scholarly attribution remains mandatory for mathematical and historical claims.

## Classical mechanics and constrained dynamics

**[Arnold-1989]** V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Graduate Texts in Mathematics 60, Springer, 1989. DOI: `10.1007/978-1-4757-2063-1`. See especially the chapters on Lagrangian/Hamiltonian mechanics and integrable systems.

**[Marsden-Ratiu-1999]** Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Texts in Applied Mathematics 17, Springer, 1999. DOI: `10.1007/978-0-387-21792-5`.

**[Carinena-Martinez-MunozLecanda-2022]** J. F. Carinena, E. Martinez, and M. C. Munoz-Lecanda, “Infinitesimal Time Reparametrisation and Its Applications,” *Journal of Nonlinear Mathematical Physics* 29 (2022), 523–555. DOI: `10.1007/s44198-022-00037-w`. Section 2 reviews the classical Sundman transformation `dt=r dτ`, collision regularization, and fixed-energy linearization of the Kepler radial equation.

## Integrable waves and KdV

**[Carretero-Frantzeskakis-Kevrekidis-2024]** R. Carretero-Gonzalez, D. J. Frantzeskakis, and P. G. Kevrekidis, “Traveling Wave Reduction, Elliptic Functions, and Connections to KdV,” in *Nonlinear Waves & Hamiltonian Systems: From One To Many Degrees of Freedom, From Discrete To Continuum*, Oxford University Press, 2024, Chapter 6. DOI: `10.1093/oso/9780192843234.003.0006`. The traveling-wave reduction gives a cubic effective potential whose elliptic solutions degenerate to solitary waves.

**[Hirota-1971]** Ryogo Hirota, “Exact Solution of the Korteweg–de Vries Equation for Multiple Collisions of Solitons,” *Physical Review Letters* 27 (1971), 1192–1194. DOI: `10.1103/PhysRevLett.27.1192`. Classical source for the exact KdV multi-soliton construction and pair-factorized collision structure.

**[Ablowitz-Segur-1981]** Mark J. Ablowitz and Harvey Segur, *Solitons and the Inverse Scattering Transform*, SIAM, 1981. DOI: `10.1137/1.9781611970883`. Standard reference for KdV inverse scattering, elastic soliton interactions, scattering data, and phase shifts.

**[Bertola-Jenkins-Tovbis-2023]** M. Bertola, R. Jenkins, and A. Tovbis, “Partial degeneration of finite gap solutions to the Korteweg–de Vries equation: soliton gas and scattering on elliptic background,” arXiv:`2210.01350`. Relevant here as a modern finite-gap/degeneration reference connecting algebraic-geometric KdV backgrounds to solitonic sectors.

## Elliptic integrals and elliptic functions

**[DLMF-5.12]** NIST Digital Library of Mathematical Functions, §5.12, “Beta Function,” especially Euler’s beta integral (Eq. 5.12.1). https://dlmf.nist.gov/5.12

**[DLMF-19]** NIST Digital Library of Mathematical Functions, Chapter 19, “Elliptic Integrals.” https://dlmf.nist.gov/19

**[DLMF-22]** NIST Digital Library of Mathematical Functions, Chapter 22, “Jacobian Elliptic Functions.” https://dlmf.nist.gov/22

**[DLMF-23.2]** NIST Digital Library of Mathematical Functions, §23.2, “Definitions and Periodic Properties,” including lattices and double periodicity of the Weierstrass `wp` function. https://dlmf.nist.gov/23.2

**[DLMF-23.3]** NIST Digital Library of Mathematical Functions, §23.3, “Differential Equations,” including Weierstrass invariants, discriminant, roots, and the cubic differential equation. https://dlmf.nist.gov/23.3

**[DLMF-23.5]** NIST Digital Library of Mathematical Functions, §23.5, “Special Lattices,” including the lemniscatic case `g3=0`, `tau=i`, and the associated special complete elliptic integral. https://dlmf.nist.gov/23.5

**[DLMF-23.19]** NIST Digital Library of Mathematical Functions, §23.19, “Interrelations,” especially Eq. 23.19.3 for Klein’s invariant `J=g2^3/(g2^3-27g3^2)`. https://dlmf.nist.gov/23.19

**[DLMF-23]** NIST Digital Library of Mathematical Functions, Chapter 23, “Weierstrass Elliptic and Modular Functions.” https://dlmf.nist.gov/23

**[Whittaker-Watson-1927]** E. T. Whittaker and G. N. Watson, *A Course of Modern Analysis*, 4th ed., Cambridge University Press, 1927. See Chapters XX–XXII for elliptic functions and their relation to elliptic integrals.

**[Lawden-1989]** Derek F. Lawden, *Elliptic Functions and Applications*, Applied Mathematical Sciences 80, Springer, 1989. DOI: `10.1007/978-1-4757-3988-0`.

## Algebraic curves, Riemann surfaces, and Jacobians

**[Forster-1981]** Otto Forster, *Lectures on Riemann Surfaces*, Graduate Texts in Mathematics 81, Springer, 1981. DOI: `10.1007/978-1-4612-5961-9`.

**[Farkas-Kra-1992]** Hershel M. Farkas and Irwin Kra, *Riemann Surfaces*, 2nd ed., Graduate Texts in Mathematics 71, Springer, 1992. DOI: `10.1007/978-1-4612-2034-3`.

**[Frauendiener-Klein-2015]** J. Frauendiener and C. Klein, “Computational approach to hyperelliptic Riemann surfaces,” *Letters in Mathematical Physics* 105 (2015), 379–400. DOI: `10.1007/s11005-015-0743-4`; arXiv:`1408.2201`. The paper treats hyperelliptic surfaces from branch-point lists or cut systems, constructs a canonical homology basis algorithmically, and computes periods of the holomorphic differentials; see especially the Introduction and Section 2.

**[McMullen-Riemann-Surfaces]** Curtis T. McMullen, *Riemann Surfaces*, Harvard Math 213b course notes. In the hyperelliptic discussion the canonical holomorphic basis is written explicitly as `x^i dx/y`. https://abel.math.harvard.edu/~ctm/math213b/home/course/course.pdf

**[Hartshorne-1977]** Robin Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics 52, Springer, 1977. DOI: `10.1007/978-1-4757-3849-0`.

**[Silverman-2009]** Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics 106, Springer, 2009. DOI: `10.1007/978-0-387-09494-6`.

## Hyperelliptic curves and Abelian functions

**[Mumford-1983]** David Mumford, *Tata Lectures on Theta I*, Progress in Mathematics 28, Birkhäuser, 1983. DOI: `10.1007/978-1-4899-2843-6`.

**[Baker-1897]** H. F. Baker, *Abel's Theorem and the Allied Theory Including the Theory of the Theta Functions*, Cambridge University Press, 1897. Historical source for Abelian integrals, inversion, and theta-function methods.

## Symbolic polynomial ideals and Gröbner bases

**[Cox-Little-OShea-2015]** David A. Cox, John Little, and Donal O’Shea, *Ideals, Varieties, and Algorithms*, 4th ed., Undergraduate Texts in Mathematics, Springer, 2015. DOI: `10.1007/978-3-319-16721-3`. See the chapters on Gröbner bases and ideal membership.

## Historical lineage

**[Kline-1972]** Morris Kline, *Mathematical Thought from Ancient to Modern Times*, Oxford University Press, 1972. Useful secondary history for the nineteenth-century development from elliptic integrals to elliptic functions and complex analysis.

**[Gray-2015]** Jeremy Gray, *The Real and the Complex: A History of Analysis in the 19th Century*, Springer, 2015. DOI: `10.1007/978-3-319-23715-2`. See the treatment of elliptic functions, Riemann surfaces, and the algebraic/analytic interaction.

## Project interpretation

Claims labelled **Shakespeare interpretation** are not claims made by the references above. The references establish classical mathematics and historical context; the process-first reinterpretation is the research program implemented and tested in this repository.
