# report-src

LaTeX sources for the **written report and poster** of the
`adaptive-latent-reasoning` project (UdeSA NLP final project).

The compiled PDFs and the rendered poster live on the `main` branch under
[`report/`](https://github.com/famatodlr/adaptive-latent-reasoning/tree/main/report).
This branch holds the editable sources; the code lives on `main` and the
`option-*` branches.

## Layout

`paper/` and `poster/` each hold one subfolder per language (paper) or per
presentation event and language (poster), so multiple poster variants can
live side by side without overwriting each other.

| Folder | What |
|--------|------|
| `paper/paper_sp/`             | Report, original **Spanish** - build `main.tex` |
| `paper/paper_en/`             | Report, **English** (ACL format) - build `main.tex` |
| `poster/poster_AI-Fest_sp/`   | A0 poster for **AI-Fest**, **Spanish** - build `poster.tex` |
| `poster/poster_AI-Fest_en/`   | A0 poster for **AI-Fest**, **English** - build `poster.tex` |
| `poster/poster_Symposium_sp/` | A1 poster for the **Symposium**, **Spanish** - build `poster.tex` (no English version yet) |

Each language pair under `paper/` shares the same figures and results. The
figure generation scripts live under `paper/paper_*/figures/scripts/` (a
shared `figstyle.py` plus one script per figure); the raw eval artifacts they
read from are under `paper/paper_*/results_test/`.

## Build

```bash
# report (English)
cd paper/paper_en && pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex

# poster (Symposium, Spanish, A1)
cd poster/poster_Symposium_sp && pdflatex poster.tex && pdflatex poster.tex && pdflatex poster.tex
```
