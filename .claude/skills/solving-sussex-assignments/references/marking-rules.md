# What actually earns and loses marks

Derived from real tutor feedback, not guesswork. Module 1 Assignment 1 scored 98/100; every
tutor comment on it, and the only lost marks, concerned the same thing.

## The closing sentence is mandatory

Verbatim tutor comments on Questions 1, 2, 4 and 9 of a 98/100 script:

> "I appreciate the neatly boxed final answer, but in the portfolio it will be appropriate to
> write a sentence of text to help close off the final answer
> (e.g.: 'Thus, state resulting from these transformations ... is : ...')"

> "Similarly: you might close with a sentence 'Therefore, the state vector ... can be simplified to ...'"

The questions that drew "This is better" and "Good exposition" were the ones that already did it.

**Every solution ends with a sentence of prose naming the result.** Not a bare formula. Not a lone
`\boxed{}`. The box may stay - the tutor liked it - but a sentence follows it.

The shape:

> Therefore, the normalisation constant is $B = 2\sqrt{\beta/3}$, which fixes the peak of the
> probability density at $4\beta/3$.

Baseline testing confirmed this is the default failure: an agent given this exact kind of question
ended both answers with `\boxed{...}` and no sentence. `assets/solution_template.tex` carries a
required slot so the sentence is structural rather than remembered.

## Exposition scales with marks

The single question that lost marks (18/20) drew:

> "Good methodology, could do with some more expositiom"

A 2-mark part can be three lines of algebra. A 15-mark part needs prose between the equations
saying what is being done and why. Use the mark allocation as the instruction it is: marks measure
the exposition expected, not just the difficulty.

## Justify every formula you invoke

Sussex briefs that permit notes say so explicitly:

> "You are permitted to use your notes and the internet to look up definitions and formulae.
> Because of this, greater emphasis will be placed in marking schemes on justifying and explaining
> the use of any such formulae."

Name the principle in words before using it, and say why it applies here. "By the Born rule" is
weaker than "the Born rule applies because the state is expanded in the orthonormal eigenbasis of
the observable being measured."

## The six steps

The module's own "Six steps to problem solving: How to gain marks" page is not in the local
exports. This is the working stand-in:

1. **Restate** what is asked, and list the givens.
2. **Write the state** in the right notation.
3. **Name the principle** you will use, in words.
4. **Do the algebra**, every step shown.
5. **Check**: units, normalisation, a limiting case, signs, probabilities in [0,1].
6. **State the answer** in a full sentence.

If the real page ever appears, replace this list with it.

## Show the check, do not just do it

A visible check earns credit and catches errors. Cheap ones that repeatedly paid off: probabilities
summing to 1, dimensional analysis, an expectation value landing between its extreme outcomes, a
sign agreeing with a sketch, a general result reproducing a special case computed earlier.
