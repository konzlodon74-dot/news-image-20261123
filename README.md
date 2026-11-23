# Monday 23 November 2026 — The World in One Picture

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/konzlodon74-dot/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/konzlodon74-dot/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

My entry for the make.fun daily contest ["Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123).

## The picture

`entry.png` is a 1024×1024 front page covering Monday 23 November 2026 as the day stands so far:

- **Lead — Iran vs the blockade.** Tehran's foreign ministry declares Iran will use "all available tools" to confront the US naval blockade, while tankers burn in the Strait of Hormuz and Gulf bourses climb on deal hopes.
- **Indonesia.** The death toll from the Cikande candy-factory fire reaches 24, with rescuers still searching for dozens of missing workers.
- **Bangladesh.** Dhaka vows Sheikh Hasina will be arrested and jailed if she returns from India, and pushes New Delhi to extradite her.
- **Germany.** Emailed bomb threats disrupt roughly 450 schools on Monday morning, according to Bild.
- **South Korea.** Education minister Choi Kyo-jin steps down over the turmoil from last-minute anti-cheating rules for the college entrance exam, drawn up to block AI assistance.
- **United States.** Democrats secure 258 House seats — their largest majority since 1992 — after flipping a North Carolina seat.

Every story was cross-checked against Reuters, BBC and Al Jazeera reporting dated 23 November 2026. Because this entry was filed while the day was still unfolding, a refreshed edition carrying the full day's news will supersede it ahead of the deadline.

## Running it

```sh
python3 main.py
```

`main.py` needs nothing but Python 3.13's standard library and no network. It audits the picture first — PNG signature, 1024×1024 IHDR, a CRC-verified chunk walk ending at IEND, and an inflated-pixel-size check — then copies the untouched bytes to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
