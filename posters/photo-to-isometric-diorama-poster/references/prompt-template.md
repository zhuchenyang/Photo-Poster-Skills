# Reference-aware generation prompt

Replace the bracketed scene observations with facts from the inspected image. Include the actual reference image in the tool request. This is prompt content, not a tool argument schema.

```text
Create a refined editorial poster from the supplied reference photograph.
Canvas: portrait 3:4, with a horizontal division at exactly half the height.
FIRST-PASS COMPOSITION PRIORITY: reserve the left text column, then establish
the complete right miniature AND visible shadow envelope before rendering details.
Use at most about 48–52% of the lower panel width and 58–64% of its height;
these are upper target ranges, not space to fill. Uniformly scale to the tighter
axis; choose smaller when uncertain. Keep generous text, divider and edge clearance.
Do not expand the model or base to fill the right area. Spacious model scale
takes priority over detail density. Achieve this in the initial generation.
Top 50%: the source photographic scene, naturally cropped without distortion,
preserving [principal subject and scene anchors].
Bottom 50%: the same recognizable scene reconstructed as a realistic miniature
isometric diorama, viewed downward at 30–45 degrees. Preserve [spatial relationships].
Show plausible terrain or construction cutaways beneath land, with visible side faces.
MANDATORY: give the miniature a clearly thick cutaway base, with readable vertical
or sloped side faces and a visible bottom edge. It must read as a volumetric terrain
section, not a thin sheet, flat photo cutout or feathered vignette. Keep thickness
proportionate and visible at thumbnail size, without making an oversized plinth.
Fit the complete base thickness and shadow within the compact model envelope.
Integrate water and terrain naturally, following the material rules below.
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
Treat the base as a natural continuation of the surface and terrain.
Water may expose a cross-section or sit naturally within surrounding terrain;
plausible soil, rock and underwater structures may continue through the model.
Not every visible volume beneath water must be pure water.
Match the reference water's color, clarity and turbidity; use natural depth shading,
light attenuation and appropriate refraction, not generic clear blue plastic/resin.
Preserve natural shore slopes and land/water transitions. Do not sever terrain
or isolate water into a separate block merely to emphasize a cross-section.
Do not add rock or stone edging around water, including an enclosing rim along
an exposed water face. Natural shoreline terrain must not become a rock border.
Avoid unrelated decorative supports, regular frames, extra pedestals or trays.
Unseen subsurface structure is plausible artistic reconstruction, not measured geology.
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
Verify that the cutaway base has appreciable thickness, readable side faces and a bottom edge even at thumbnail size. Reject a thin sheet, flat cutout or feathered vignette. Its materials must continue the scene naturally, and its full thickness must fit within the model envelope.

Review the full poster at thumbnail size for optical balance. For a text-free 1200 × 800 lower panel, a useful starting envelope is at most 840 × 600, scaled proportionally and positioned with clear space above the subject and below the shadow. Narrow or tall scenes may occupy less width. Check actual four-sided clearance rather than relying on a total background-area percentage.

With default text, verify the reserved left column, right-positioned complete model, readable spelling, and balanced text/model spacing; do not apply the centered text-free envelope to this layout.

For water scenes, review natural terrain continuity, authentic water appearance and coherent shoreline joins. Plausible soil, rock and underwater structure are allowed; do not force an isolated pure-water block. Reject rock edging around water and unrelated decorative supports. Unseen structure and water depth are artistic, not measured.
