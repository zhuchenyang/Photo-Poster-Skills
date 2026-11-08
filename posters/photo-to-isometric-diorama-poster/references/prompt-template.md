# Reference-aware generation prompt

Replace bracketed observations with facts from the inspected image and finalized copy. Include the actual reference image in the tool request. Use the same observation-driven template across scenes; include only properties supported by the reference. This is prompt content, not a tool argument schema.

```text
Create a refined editorial poster from the supplied reference photograph.
Canvas: portrait 3:4, with a horizontal division at exactly half the height.
The upper photograph must end at the exact midpoint. Preserve the selected source
crop intact. If it cannot fill the upper 50% without stretching or discarding
established content, generate only the missing extension beyond its boundaries.
Continue observed boundary content, perspective, scale, lighting and texture seamlessly;
do not squeeze the crop, repeat obvious patterns or invent a new focal subject.
FIRST-PASS COMPOSITION PRIORITY: reserve the left text column, then establish
the complete right miniature AND visible shadow envelope before rendering details.
Use at most about 48–52% of the lower panel width and 58–64% of its height;
these are upper target ranges, not space to fill. Uniformly scale to the tighter
axis; choose smaller when uncertain. Keep generous text, divider and edge clearance.
Do not expand the model or its supporting structure to fill the right area.
Spacious model scale takes priority over detail density. Achieve this initially.
Top 50%: the source photographic scene, naturally cropped without distortion,
preserving [principal subjects and distinguishing features].
Bottom 50%: the same recognizable subjects and scene reconstructed as a realistic
miniature isometric-style diorama, viewed downward at 30–45 degrees.
Preserve [subject identity, proportions, pose or configuration, spatial and support relationships].
Make the reconstruction visibly three-dimensional at thumbnail size through coherent
volume, proportional thickness, readable side surfaces, overlap and lighting.
Make foreground volumetric materials' depth readable in the base or exposed side section.
For foreground water present in the reference, show a perceptible water column below
the surface, with a visible depth-bearing side face and natural color attenuation
consistent with observed clarity and turbidity. Depth does not require transparency.
Do not substitute an opaque soil/stone slab for water depth or impose clear blue resin.
Maintain adjoining substrate continuity without forcing a pure-water block or adding
an enclosing rim. Inferred depth is artistic, not measured; fit it within the envelope.
Derive [supporting geometry and necessary inferred surfaces] from visible evidence.
Retain source-supported structure and material continuity; do not force a thick terrain
block, ground, underground layers or a pedestal onto a subject that does not support them.
Infer only the minimum unseen geometry needed for this view; do not fabricate major
features or an environment to satisfy the camera style. Inferred parts are plausible
artistic reconstruction, not factual recovery.
Keep the full model silhouette, any supporting structure and visible shadow inside
the bottom half and within the compact composition envelope.
Use a spacious left-text/right-model editorial layout. Reserve a left-aligned
text column around 30–35% of the lower panel width first, then place the complete
miniature on the right. Uniformly scale it to keep the full silhouette and shadow
clear of text, divider and all outer edges. Optically balance text and model
together. Preserve generous four-sided breathing room; do not fill the right area.
Treat all copy as one vertically centered three-tier text block. Use one shared
left alignment axis about 3.5–4.5% of full canvas width from the left edge. Place
the block's optical center about 48–50% down the lower panel, with the complete
block usually occupying about 38–43% of lower-panel height. Do not vertically
center only the headline or distribute the three tiers independently.
English copy, derived from observed content, concise and restrained, with emotional
tone and energy supported by the photograph rather than a fixed scene-to-mood pairing:
Overline (clean geometric/neo-grotesque sans comparable to Avenir Next, Helvetica
Neue or Inter; semibold uppercase; 0.20–0.28 em tracking; about 2.0–2.3% of canvas
width, or 24–28 px at 1200 × 1600): "[2–3 subject-specific words]"
Headline (elegant regular-weight editorial serif comparable to Cormorant Garamond,
Canela or Libre Baskerville; not bold; about 5.0–5.6% of canvas width, or 60–67 px
at 1200 × 1600; 0.95–1.05 em line height; 2–3 balanced lines):
"[3–6 words, explicit line breaks]"
Supporting copy (same sans family as overline, regular sentence case; about
2.2–2.6% of canvas width, or 26–31 px at 1200 × 1600; two lines at 1.18–1.28 em
line height): "[about 8–14 words total]"
Use about 0.65–0.80 headline em of visible vertical space between overline and
headline, and again between headline and supporting copy. Scale all three tiers
and both gaps together; preserve their hierarchy and the block's vertical center.
Render the supplied final copy verbatim in dark charcoal with clear contrast.
Use one visible subject or scene anchor, simple natural English and at most one
gentle metaphor. No stock slogans, invented facts or inferred private emotions.
Keep text in the lower half.
If crowded, pull back and uniformly shrink the entire scene; preserve the proportions
and complete form of the actual subject. Do not crop or flatten it to fit.
Materials: [observed material identities, colors, textures, optical properties and boundaries].
Preserve each material's identity and visually relevant physical properties, including
opacity, transparency and reflectance as supported by the image. Simplify fine detail
for miniature scale without replacing material categories.
Maintain [observed transitions, attachments and continuous structures]. Do not isolate
components merely to showcase a cross-section or impose a generic optical treatment.
Do not apply a uniform substitute material or color that erases real differences.
Preserve genuinely uniform, single-material or single-color subjects when supported
by the reference, including plaster or resin; follow explicit user overrides.
Do not invent borders, rims, frames, trays or decorative supports. Preserve these
features when genuinely present in the reference.
Material authenticity takes priority over spatial accuracy, sculptural expression
and stylistic material uniformity.
Use refined geometry, soft studio light, realistic contact shadows, and a clean
warm-neutral background. Add only the specified editorial copy; do not add logos,
border decoration or watermarks. Preserve existing structural features.
MANDATORY CONTACT SHADOW: express volume and support relationships through natural
shadows at actual contact areas. Keep the darkest, comparatively sharper occlusion
beneath supported forms and near contacts, then soften and lighten it with distance
according to geometry, lighting and actual separation. Do not add an elevated base
solely to create a shadow. Avoid uniform halos, duplicated forms, arbitrary glows
or hard floating gaps. Keep the complete visible-shadow envelope inside the model
area and away from the text, divider and outer edges.
```

If the user requests no text, remove the copy instructions and replace all left-column/right-model placement instructions with the centered text-free layout and sizing guidance in SKILL.md. Follow explicit language, copy and style overrides.

For a separate lower-scene generation, remove the top-photo requirement and request a lower-panel asset to be placed inside the 3:4 poster's lower half. Keep its composition wide enough for a 3:2 panel. Composite the source crop above it, with any necessary boundary extension; do not squeeze a complete portrait model into the panel. A generative pass does not guarantee pixel fidelity.

## Review guide

For a 1200 × 1600 output, the split is y=800 and each panel is 1200 × 800. Use another resolution if the tool requires it, while retaining the final ratio. Verify actual output dimensions rather than assuming the prompt enforced them.

Verify that the upper source crop's established content remains intact and only missing boundary area was extended. Reject stretching, squeezed proportions, visible extension seams, repeated texture bands or newly invented focal subjects. Measure the divider position after generation.

Use the same reference-based checks for every photograph:

- Compare subject identity, recognizable features, proportions, pose or configuration, and spatial and support relationships with the source. Confirm that camera reconstruction has not invented major features or an environment.
- Check material identities, colors, textures, optical properties, boundaries and connections against the image. Preserve real material differences and genuinely uniform appearances. Inferred hidden geometry must be minimal and structurally plausible.
- Verify readable volume, foreground material depth and source-appropriate thickness at thumbnail size. Foreground water must have a perceptible below-surface water column in the base or exposed side, rather than only a surface painted on a solid slab; retain the reference's optical character and connected substrate. Reject flat photo cutouts and unsupported terrain blocks or decorative supports. Retain borders, frames and supporting structures genuinely present in the source; reject invented additions.
- Check the entire silhouette, any supporting structure and visible shadow against all four margins. For a text-free 1200 × 800 lower panel, a useful starting envelope is at most 840 × 600, scaled proportionally with clear space above the subject and below the shadow. Narrow or tall subjects may occupy less width.
- With default text, verify the reserved left column, shared left alignment axis, complete three-tier block centered optically at about 48%–50% of lower-panel height, serif/sans hierarchy, specified relative type sizes, within-tier line heights, 0.65–0.80 headline-em inter-tier gaps, complete right-positioned model, spelling, readability and balanced spacing. Do not apply the centered text-free envelope to this layout. Confirm that the copy references visible content and its tone fits the photograph.
- Verify natural shadows at actual contact areas, consistent with geometry and light direction. Reject uniform glows, duplicated forms, hard floating gaps and shadows intruding into text or margins. Do not require a raised base.

Review the complete poster at intended viewing size and thumbnail size. Correct concrete defects and disclose unresolved deviations; do not claim verification without viewing and measuring the output.
