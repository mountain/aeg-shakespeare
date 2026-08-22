# Finite-family calibration map

This note is intentionally short. It records the executable sequence that
supports the first frozen finite-family API:

```text
Translation I
    T_a T_b = T_{a+b}
    -> ProcessFamily
    -> ProcessCharacter

Dilation I
    S_a S_b = S_{ab}
    -> same ProcessFamily / ProcessCharacter API
    -> no new core abstraction

A/M I
    scale acts on translation parameter b -> a b
    -> FamilyAction
    -> character transport xi -> a xi
    -> scalar-character invariance obstruction

Galilean I
    spacetime translation (a,s)
    boost shear (a,s) -> (a+v s,s)
    -> same ProcessFamily / ProcessCharacter / FamilyAction API
    -> missing mass term retained as unresolved residual
```

The API is frozen at this point until a later vignette forces either an
operator-valued response object or a repeated central/cocycle residual.
