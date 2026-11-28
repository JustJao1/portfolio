# Developer portfolio

Personal portfolio of João Victor da Silva, showcasing software projects and interactive demonstrations.

[Visit portfolio](https://joaovictorsilvadev.vercel.app/) · [GitHub profile](https://github.com/JustJao1)

The static website is in `index.html`. Open it in a browser or serve it with `python -m http.server 8080`. Each software project is maintained in a separate repository.

# Ownership and maintenance

Project owner and maintainer: [João Victor da Silva](https://github.com/JustJao1).

Independent portfolio project developed with AI assistance. Original project materials remain under their owner's rights; no general license is granted by public availability. Third-party components retain their respective licenses.


## Desktop software

- [LinkPilot v0.7.1 — experimental Windows application](https://github.com/JustJao1/linkpilot). Project documentation; the original executable is retained separately and complete source is not currently published.


## Engineering evidence / Evidências de engenharia

[Published portfolio section](https://justjao1.vercel.app/#engineering) · [Measured results and scope](evidencias/engineering-quality-2026-11-28.md) · [CI](https://github.com/JustJao1/portfolio/actions/workflows/verify-engineering.yml).

Run `python tools/verify_engineering.py` to check navigation and evidence links. Browser checks: `npm install --prefix tools/browser`, `npx --prefix tools/browser playwright install chromium`, `npm --prefix tools/browser test`. Tests use a local server, no production data. / Os testes verificam idioma, tema, filtros e layout responsivo sem usar dados de produção.
