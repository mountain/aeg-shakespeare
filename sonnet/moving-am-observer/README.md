# Sonnet — Moving A/M Observer Contract (S2′)

The static Hidden A/M Noether search ended with a structural no-go: a frozen
observer in the same product-affine group conjugates stabilizers and therefore
cannot reveal a missing stabilizer dimension.  That result narrows the next
question; it does not reject canonicalization.

This folder freezes the minimum executable contract for the next search:

```text
instantaneous normalization N(data, observer)=0
                         |
                         | differentiate DN=0
                         v
                 observer connection
                         |
                         v
physical process = canonical shape + observer transport
                         |
                         v
                exact reconstruction
```

## Current calibration

`moving_observer_contract.py` runs the known Riccati positive control

`x'=(x-t)(x-t-1)`, with `x=t+y`.

The normalization consists of the two instantaneous roots.  Their derivative,
not a supplied observer law, gives `r'=1,d'=0`.  The physical shape
`y²-y` and transport `-1` reconstruct the canonical lift `y'=y²-y-1` exactly;
its coefficient-jet complexity drops from two to zero.  A frozen observer fails
the differentiated normalization with residual `(1,-1)`.

The red team adds `epsilon*x³`.  Affine transport has degree at most one, so the
cubic coefficient survives in the canonical shape and observed equation.  The
certificate therefore cannot obtain simplicity by silently deleting completion
payload outside its declared observer grammar.

## What this does not establish

This calibration uses the existing exact SymPy constraint backend.  It is not
an AMJet construction, does not discover the root normalization blindly, and
does not reopen the 166 static-frontier expressions with a successful dynamic
observer.  It only makes four future proof obligations executable:

1. normalization must be stated without observer rates in the oracle input;
2. observer motion must be induced by differentiating normalization;
3. shape and transport must be separated; and
4. their lift must reconstruct the original process exactly, including
   out-of-grammar residual payload.

The next falsifiable gate is to derive the required local jet from bounded AM
histories, then search a frozen normalization grammar blindly.  If no
normalization both preserves the task payload and lowers the declared
representation cost, the moving-observer branch also closes negatively.
