# Return 16

A personal tech blog about mainframes, z/OS, computing history, and life in STEM. Tutorials, tips, and tales from the sysprog trenches.

> **"Mainframing is for everyone."**

---

## Pages

| Page | File | Description |
|---|---|---|
| Home | `index.html` | Landing page with category cards and latest posts |
| Mainframe | `mainframe/index.html` | Posts about IBM Z, z/OS, RACF, ISPF, JCL, SDSF, and sysprog life |
| Computing & Tech | `computing/index.html` | General computing, tech history, programming, women in STEM *(coming soon)* |
| Resources | `resources.html` | Curated list of mainframe resources — blogs, tutorials, emulators, freeware |
| Post History | `history.html` | Every post in reverse chronological order |
| About | `about.html` | About the author and the blog |

---

## Posts

All post files live in the `posts/` directory.

---

## File Structure

```
Blog/
├── index.html              # Home page
├── about.html              # About page
├── history.html            # Post history (all posts, reverse chronological)
├── resources.html          # Curated mainframe resources
├── post-template.html      # Template for new posts
├── .nojekyll               # Disables Jekyll processing (GitHub Pages)
│
├── mainframe/
│   └── index.html          # Mainframe category page
│
├── computing/
│   └── index.html          # Computing & Tech category page
│
├── posts/                  # Individual post pages (one .html file per post)
│
├── css/
│   └── style.css           # Single shared stylesheet
│
└── images/
    ├── pink-bow.png         # Site logo / header icon
    └── sparkle-heart.png    # Favicon and decorative icon
```

---

## Notes

- **No build step** — the site is plain HTML and CSS with no frameworks or dependencies.
- **Hosted on GitHub Pages** — the `.nojekyll` file disables Jekyll so the site is served as-is.
- **Adding a new post** — copy `post-template.html` into `posts/`, write the content, then add an entry to `history.html` and the relevant category page, and update the latest posts section on `index.html`.
- **Styling** — all styles are in `css/style.css`. There is one shared stylesheet used by every page.
