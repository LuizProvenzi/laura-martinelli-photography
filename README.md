# Laura Martinelli — Photography

A single-page landing site for photographer Laura Martinelli.

A portrait of her, her name, and twenty-one photographs. Nothing else — no menu, no
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

The gallery is a fixed editorial grid, sketched by hand first: rows of three,
broken by a full-width banner (photo 7) and a wide pair (17 and 18). Every tile
in a row shares one shape, so each row lands on a single height; photos fill
their frames and are cropped to fit, with a focal point chosen per photo so the
subject survives. Click any one to open it large and uncropped. The same grid
scales down on a phone rather than being rearranged.

Plain HTML, CSS and JavaScript in a single file. No framework, no build step,
no dependencies. Photos load lazily, as small WebP variants on phones (about 1 MB for all
twenty-one) and larger ones on wide screens.

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

The script resizes, converts to WebP and fixes EXIF rotation. Photos are named
by position (`1.jpg` … `21.jpg`), so replacing one in `originals/` and re-running
is all it takes.

Each `<figure class="tile">` in `index.html` carries two values:

- `--shape` — the row's width / height; keep it the same for every tile in a row.
- `--pos` — which part of the photo survives the crop (`50% 50%` is centre,
  `50% 80%` keeps the lower part). Omit it to centre.

`tile--full` spans the whole row, `tile--half` takes half of it.

## Deploying

Push to a public GitHub repository, then **Settings → Pages → Deploy from a
branch → `main` / root**. Live in a couple of minutes; every push republishes.

For a custom domain, add it under the same settings screen and point the DNS at
GitHub's servers (`185.199.108-111.153`), then enable *Enforce HTTPS*.
