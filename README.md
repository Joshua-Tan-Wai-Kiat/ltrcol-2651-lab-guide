# LTRCOL-2651 lab guide

AI Receptionist for Webex Calling — Cisco Live Melbourne.

This MkDocs site contains an introduction and six lab tasks converted from
Hussain Ali's Word lab guide. The original document is not needed to build the site.

## Preview locally

Use Python 3.12 or later:

```sh
python -m venv .venv
```

Activate the environment (`.venv\Scripts\Activate.ps1` in PowerShell, or
`source .venv/bin/activate` on macOS/Linux), then:

```sh
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open `http://127.0.0.1:8000`. Changes to Markdown appear automatically.

## Edit directly in GitHub (no software installation)

1. Sign in to GitHub as the repository owner.
2. Open the published lab page and click its pencil **Edit this page** button.
3. Edit the Markdown text. Use **Preview** to check formatting.
4. Click **Commit changes**, describe your edit, and commit to **main**.
5. GitHub Actions rebuilds and publishes the update. Check the **Actions** tab for completion.

You can also open `docs/index.md` or a file in `docs/tasks/` in this repository and click the pencil button.
For a reviewed change, create a branch and pull request instead; publishing occurs when it merges into main.

Use `## Step title` for step headings, `**bold**` for emphasis, and numbered lists for instructions.
Upload new screenshots to `docs/assets/images/`, then reference them from a task as
`![Description](../assets/images/filename.png)`. Check screenshots for passwords and session access links before uploading.

Edit the Markdown files for website changes; replacing the Word document does not update the website.
Do not edit the generated `site/` folder. Navigation and site title are configured in `mkdocs.yml`.

## Project files

- `docs/index.md`: introduction, objectives, topology, and overview.
- `docs/tasks/`: one Markdown file per task, with steps as headings.
- `docs/assets/images/`: extracted document images.
- `mkdocs.yml`: navigation, theme, and Markdown extensions.
- `docs/stylesheets/extra.css`: layout and colors.
- `docs/javascripts/image-viewer.js`: keyboard-accessible screenshot enlargement.
- `CONTENT_REVIEW.md`: source inconsistencies and conversion notes.

Maintain the Markdown pages as the source of truth for website updates.
The screenshot files retain their source filenames for traceability.

## Validate

```sh
python -m mkdocs build --strict
python scripts/check_site.py
```

The build reports missing Markdown targets. The checker verifies generated page
links, anchors, image references, and the seven required pages. It does not log
into lab applications or validate the operational state of a dCloud session.

## GitHub Pages

The included `.github/workflows/pages.yml` builds and publishes every push to
`main`. Pull requests build and validate without publishing.

1. Push this project to a GitHub repository with default branch `main`.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions**.
3. Open **Actions → Build and publish lab guide** to watch deployment, or run it
   manually with **Run workflow** after enabling Pages.
4. The deployment job provides the published URL.

The workflow derives the site URL from the repository owner and name. No personal
access token is stored in the project; deployment uses GitHub's workflow token.

This public edition excludes credential values, password construction rules, and screenshots containing credentials or session access details. Obtain login details privately from your assigned session or instructor. The original Word file and private conversion artifacts are not part of this repository.
