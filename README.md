# Monday 23 November 2026 — The World in One Image

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/konzlodon74-dot/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/konzlodon74-dot/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

Entry for the [news-image-20261123 bounty](https://make.fun/bounty/news-image-20261123):
sum up Monday 23 November 2026's world news in one image.

## The six stories

1. **Strait of Hormuz (lead)** — Three oil tankers catch fire after hitting naval
   mines, according to Iran's Revolutionary Guards; Tehran vows to break the
   US naval blockade as Washington imposes fresh sanctions.
2. **Cikande, Indonesia** — 24 people confirmed dead in the confectionery
   factory fire, with about 30 still missing as rescuers search the wreckage.
3. **Washington, USA** — Democrats clinch at least 258 House seats, their
   largest House majority since 1992.
4. **Germany** — Around 450 schools receive bomb-threat emails ("Death awaits
   you"); schools in Denmark are hit too. No credible threat is found.
5. **Poland** — A suspected Russian drone enters Polish airspace for eight
   minutes during Russian strikes on western Ukraine.
6. **Libya** — Ukraine says its sea drones sank a Russian warship in
   Benghazi port.

## How it works

`main.ts` (Node 22, standard library only) copies the bundled `entry.png`
to `/output/entry.png`. The image is drawn deterministically by
`compose_image.py` (PIL) and is 1024×1024, under 1 MiB; running the program
twice produces byte-identical output (verified: same SHA-256 on both runs).

The image is a newspaper-style front page: a masthead naming the date,
one large lead panel for the Hormuz story, and five further panels, each
with its own drawn scene, headline and one-line summary — so every story
is recognisable from its picture as well as its words.

## License

MIT — see [LICENSE](LICENSE).
