# Laura Martinelli — Photography

A single-page landing site for photographer Laura Martinelli.

A portrait of her, her name, and seven photographs. Nothing else — no menu, no
copy, no contact form. The work carries the page.

**Live:** <https://luizprovenzi.github.io/laura-martinelli-photography/>

## The idea

The page opens on a split: her portrait on one side at its own proportions, her
name alone in the space left over. A 3:4 photograph cannot fill a widescreen the
way a landscape hero does without being cropped to a strip, so the layout gives
way instead of the image.

That opening band is dark, in the tone sampled from the portrait's own
background. The photograph is 69% near-black; against white it read as a slab
cut out and pasted down. Matching the surround lets it dissolve into the page.
The gallery below returns to a warm off-white — not pure white, which makes the
drop from black a harder landing than it needs to be.

The gallery itself is justified, the way a printed contact sheet reads. Photos keep their
original proportions and are never cropped; each row scales to fill the page
width, so images sitting side by side always match in height. Click any one to
open it large.

Rows are not fixed. For the viewport at hand the page works out how many photos
belong on each line — four across on a desktop, two on a tablet, one at a time
on a phone — favouring the largest photos that still fit the screen without any
of them turning into a thumbnail.

Once it comes down to a single column the rule inverts: rather than stretch every
frame to the full width, which would leave each one a different height, they all
share one height. Same size down the page, widths free to follow the shape of
each photograph, every left edge flush with the name in the header.

Plain HTML, CSS and JavaScript in a single file. No framework, no build step,
no dependencies. The whole page weighs about 1.4 MB — down from 40 MB of
camera originals.

## Structure

```
laura-martinelli-photography/
├── index.html          # the entire page
├── photos/
│   ├── originals/      # straight from the camera — local only, gitignored
│   └── web/            # optimized .webp, this is what ships
└── scripts/
    └── optimize.py     # originals -> web
```

`photos/originals/` is deliberately kept out of the repository: GitHub Pages
serves every file it holds, and the site has no use for them. Keep a backup of
that folder — it is the only source `optimize.py` can work from.

## Changing the photos

```bash
pip install pillow
python scripts/optimize.py
```

The script resizes, converts to WebP, fixes EXIF rotation, and prints each
image's `--ratio`. Copy that value into the matching `<figure class="tile">` in
`index.html`, along with the new filenames.

That is the whole edit — photos are a flat list, so adding or removing one needs
no layout changes. Rows are recalculated on the fly.

## Deploying

Push to a public GitHub repository, then **Settings → Pages → Deploy from a
branch → `main` / root**. Live in a couple of minutes; every push republishes.

For a custom domain, add it under the same settings screen and point the DNS at
GitHub's servers (`185.199.108-111.153`), then enable *Enforce HTTPS*.
