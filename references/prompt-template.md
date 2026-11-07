# Reference-aware generation prompt

Replace the bracketed scene observations with facts from the inspected image. Include the actual reference image in the tool request. This is prompt content, not a tool argument schema.

```text
Create a refined editorial poster from the supplied reference photograph.
Canvas: portrait 3:4, with a horizontal division at exactly half the height.
Top 50%: the source photographic scene, naturally cropped without distortion,
preserving [principal subject and scene anchors].
Bottom 50%: the same recognizable scene reconstructed as a realistic miniature
isometric diorama, viewed downward at 30–45 degrees. Preserve [spatial relationships].
Show a plausible cutaway of terrain or construction, with visible side faces.
Keep the full model silhouette and its contact shadow inside the bottom half.
Use a spacious left-text/right-model editorial layout. Reserve a left-aligned
text column around 30–35% of the lower panel width first, then place the complete
miniature on the right. Uniformly scale it to keep the full silhouette and shadow
clear of text, divider and all outer edges. Optically balance text and model
together. Preserve generous four-sided breathing room; do not fill the right area.
English copy, derived from the observed scene, quiet and contemplative:
Overline (small uppercase, tracked sans-serif): "[2–3 scene-specific words]"
Headline (regular serif, 2–3 balanced lines): "[3–6 words, explicit line breaks]"
Supporting copy (smaller type, two lines): "[about 8–14 words total]"
Render the supplied final copy verbatim in dark charcoal with clear contrast.
Use one visible scene anchor and fitting mood, simple natural English and at most
one gentle metaphor. No stock slogans or invented facts. Keep text in lower half.
If crowded, pull back and shrink the entire scene; preserve the proportions
and complete form of the actual subject. Do not crop or flatten it to fit. More background
is preferable to a model that crowds the divider or edges.
Materials: [surface -> corresponding material and plausible cutaway mapping].
Soil stays soil, gravel stays gravel, rock stays rock, grass stays vegetation;
wood, masonry, brick, and concrete keep their authentic physical identities.
Preserve material boundaries and natural transitions. Simplify fine texture for
miniature scale only. Never unify the scene into plaster, ivory resin, or beige.
No unrelated decorative pedestal. Material authenticity takes priority over
spatial accuracy, sculptural expression, and stylistic material uniformity.
Use refined geometry, soft studio light, realistic contact shadows, and a clean
warm-neutral background. No additional text beyond the specified copy, logo, border decoration, or watermark.
```

If the user requests no text, remove the copy instructions and center the complete model with generous four-sided margins; use the text-free sizing guidance in SKILL.md. Follow explicit language and copy overrides.

For a separate lower-scene generation, remove the top-photo requirement and request a lower-panel asset to be placed inside the 3:4 poster's lower half. Keep its composition wide enough for a 3:2 panel. Composite the source crop above it; do not squeeze a complete portrait model into the panel.

## Review guide

For a 1200 × 1600 output, the split is y=800 and each panel is 1200 × 800. Use another resolution if the tool requires it, while retaining the final ratio. Verify actual output dimensions rather than assuming the prompt enforced them.

Review mixed-material scenes especially carefully: a gravel path through soil and grass must retain three distinct surface categories; a stone platform must not become a plaster slab. The base should explain the scene's ground or construction rather than serve as an unrelated display stand.

Review the full poster at thumbnail size for optical balance. For a text-free 1200 × 800 lower panel, a useful starting envelope is at most 840 × 600, scaled proportionally and positioned with clear space above the subject and below the shadow. Narrow or tall scenes may occupy less width. Check actual four-sided clearance rather than relying on a total background-area percentage.

With default text, verify the reserved left column, right-positioned complete model, readable spelling, and balanced text/model spacing; do not apply the centered text-free envelope to this layout.
