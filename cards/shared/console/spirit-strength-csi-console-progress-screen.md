---
id: spirit-strength-csi-console-progress-screen
title: 'The Progress Screen reports Avg m/s, Elapsed Time, Total lb, KCAL and Reps while the set runs, over a blue range-of-motion bar'
kind: fact
question: 'What does the Spirit i-Strength console show during a set on the csi-cpsp and csi-lrow?'
asked_as:
- 'what do the numbers on the i-strength screen mean while i lift'
- 'what is avg m/s on the spirit weight machine'
- 'what is the blue bar on the i-strength screen'
- 'does the touchscreen count my reps while i work out'
keywords:
- 'progress screen'
- 'avg m/s'
- 'elapsed time'
- 'total lb'
- 'kcal'
- 'reps'
- 'progress bar'
- 'range of motion'
- 'end set'
- 'live data'
facets:
  brand:
  - spirit
  product_line: strength
  model: '*'
  applies_to:
  - csi-cpsp
  - csi-lrow
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-strength-csi-console-summary-screen
see_also:
- spirit-strength-csi-console-summary-screen
- spirit-strength-programs-pure-training-mode
- spirit-strength-programs-four-i-strength-training-modes
source:
  ref: spirit-strength-csi-cpsp-owners-manual
  locator: 'TRAINING MODES - PURE CONTINUED, and the matching CONTINUED page in each of the other three modes, printed p. 29 of the CSI-CPSP book (PDF p. 30) and p. 25 of CSI-LROW (PDF p. 26). The two books'' console chapters are identical at 99.2% word level from the PDF text layer, the only differences being the page numbers; every figure below was read from the native text layer of both PDFs and cross-checked against a 300 dpi tesseract --psm 4 render of the page.'
  extracted_at: '2026-09-10'
---

> As the exercise begins, the Progress Screen displays and collects real time data for the exercise
> including Milliseconds, Elapsed Time, Total lb, KCAL, Repetitions.

## The five live figures, as the manual defines them

| Figure | What the manual says it is |
|---|---|
| **Avg m/s** | *provides possible benefits with athletic performance or physical therapy measures and may not be relevant to most users* |
| **Elapsed Time** | the cumulative time counting upwards |
| **Total lb** | the cumulative resistance lifted during the entire set |
| **KCAL** | the cumulative kcals for the entire set |
| **Reps** | the cumulative repetitions for the set; **this measure resets to zero with each set** |

The manual's own prose calls the first figure *Milliseconds* in the list and *Avg m/s* in the
definition beneath it, and the screen is labelled **Avg m/s**. Read it as the average movement speed.

## What else is on the screen

- **A Progress Bar illuminated in blue.** It *slides to the right to visually display the range of
  motion for each of the repetitions* - it is a range-of-motion indicator, not a set or workout
  progress bar.
- **The resistance control**, live: the + and - buttons and the finger slide work here exactly as
  they do on the Setup Screen. On Isokinetic and Elastic the equivalent control is the Movement
  Speed or Resistance Level selector.
- **See Chart** in the upper corner, which swaps the figures for a graph - a bar graph in Pure and
  Eccentric, a current-against-previous line graph in Isokinetic and Elastic. Each mode card carries
  its own chart, starting at `spirit-strength-programs-pure-training-mode`.
- **End Set**: *When the desired repetitions of the exercise are completed, press End Set.*

**Isokinetic drops Avg m/s.** Its Progress Screen page lists only Elapsed Time, Total lb, KCAL and
Repetitions - which makes sense in a mode that holds speed constant. The other three modes list all
five.
