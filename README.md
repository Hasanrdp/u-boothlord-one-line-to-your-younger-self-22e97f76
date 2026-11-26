[![make.fun](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76)
[![rank](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/Hasanrdp/u-boothlord-one-line-to-your-younger-self-22e97f76/rank.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76)
[![reward](https://make.fun/badge/u-boothlord-one-line-to-your-younger-self-22e97f76/Hasanrdp/u-boothlord-one-line-to-your-younger-self-22e97f76/reward.svg)](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76)

# One Line to Your Younger Self

Entry for the [make.fun One Line to Your Younger Self competition](https://make.fun/bounty/u-boothlord-one-line-to-your-younger-self-22e97f76): one line, in English, that the writer would send back to his younger self if a single line were all he got.

## The line

> Put the phone down at 3 a.m., kid — the free tools will still be there tomorrow, but the sleep you trade for them won't come back.

130 characters, one sentence, one breath. It is spoken straight to the younger self, and it names a habit only this writer's older self could name: the late nights spent hunting free tools on his phone, trading sleep for them. The turn is the trade itself — the tools wait, the sleep does not — and it stings a little, the way a hard-won lesson should, without turning sentimental.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. It is fully deterministic: no randomness, no clock, no network, no input, so every run writes byte-identical output. Before writing, it verifies its own output against the gate — 1 to 200 characters, not only whitespace — and against a pinned character count (130), byte count (132) and sha256, and exits non-zero without writing anything if any check fails.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
