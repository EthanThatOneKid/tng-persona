# TNG Persona Dataset Report

- Dialogue rows: 59750
- Computer interactions: 517
- Speaker profiles: 722
- Enterprise computer training rows: 353
- Character-conditioned training rows: 59037

## Dialogue by season

| Season | Dialogue lines |
|---|---:|
| 1 | 9353 |
| 2 | 7929 |
| 3 | 8569 |
| 4 | 8596 |
| 5 | 9098 |
| 6 | 7970 |
| 7 | 8235 |

## Most frequent speakers

| Speaker | Lines | Episodes | Avg words | Question rate |
|---|---:|---:|---:|---:|
| PICARD | 11969 | 176 | 11.91 | 0.293 |
| RIKER | 7012 | 176 | 9.84 | 0.3 |
| DATA | 6078 | 173 | 13.23 | 0.13 |
| LAFORGE | 4325 | 168 | 12.9 | 0.199 |
| WORF | 3693 | 173 | 8.91 | 0.126 |
| TROI | 3155 | 163 | 11.38 | 0.26 |
| CRUSHER | 3107 | 152 | 13.18 | 0.232 |
| WESLEY | 1369 | 68 | 9.55 | 0.246 |
| COMPUTER | 527 | 107 | 7.54 | 0.038 |
| TASHA | 504 | 25 | 10.37 | 0.183 |
| PULASKI | 495 | 20 | 12.1 | 0.218 |
| GUINAN | 481 | 29 | 11.57 | 0.304 |

## Main speakers addressing the computer

| Speaker | Interactions |
|---|---:|
| PICARD | 116 |
| LAFORGE | 102 |
| DATA | 90 |
| RIKER | 50 |
| CRUSHER | 46 |
| TROI | 19 |
| WORF | 14 |
| BARCLAY | 10 |
| K'EHLEYR | 8 |
| WESLEY | 7 |
| SCOTT | 4 |
| LYNCH | 3 |

## Notes

- The enterprise computer subset is best suited for terse operational personas.
- The character-conditioned JSONL keeps a speaker label in metadata so you can filter for Picard, Data, Guinan, or any other voice later.
