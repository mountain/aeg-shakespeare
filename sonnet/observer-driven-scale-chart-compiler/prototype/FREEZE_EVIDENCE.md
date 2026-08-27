# Pre-reveal freeze evidence

The strict held-out was executed in a shared scratch workspace before this
Sonnet was copied into its public repository path.

The original manifest uses workspace-relative paths beginning with
<code>workstreams/scale_compiler/</code>. Those paths intentionally remain
unchanged in <code>FREEZE_MANIFEST.sha256</code>; changing the manifest after
reveal would destroy the evidence record.

The source, tests, README, demo, project file, and frozen contract were copied
byte-for-byte into this <code>prototype/</code> directory. Their individual
SHA-256 values therefore match the corresponding lines in the original
manifest after replacing only the path prefix.

The composite SHA-256 of the original sorted manifest lines is:

~~~text
377972b2f674a06ffb66a9e99a7ac992744d214f520cacff9ac61f1a14253680
~~~

The held-out commitment made before reveal is:

~~~text
475733c57a34b3cfe2990445f38965e1d277329b7b38795ae0f85cd289f32a89
~~~

<code>HELD_OUT_RESULT.json</code> records the discoverer input, exact output,
certificate checks, and the statement that no frozen implementation file
changed after reveal. This explanatory file was added during public
integration and is not part of the pre-reveal manifest.
