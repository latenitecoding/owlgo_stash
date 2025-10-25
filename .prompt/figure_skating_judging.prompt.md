Anissa has just finished her figure skating routine and is anxiously awaiting her scores. The way scoring works at this specific event is a little peculiar - each figure skater is evaluated by several judges and the scores are averaged to give a final score.

Jolie is managing the software used to compile the scores and notices that a hacker has gotten in and inserted many fake evaluations. She knows exactly how many scores she should expect, so she will manually invalidate evaluations until the number of evaluations matches the number of judges she knows actually submitted evaluations.

The problem is, Jolie doesn’t know which evaluation to invalidate. She decides to use the following metric for assessing the badness of a collection of scores after invalidating enough to get the number of evaluations to match the number of judges:

1. Compute the arithmetic mean of all the evaluations from the chosen collection.

2. Compute the squared deviation of each evaluation in the chosen collection to the given arithmetic mean. That is, if the mean is mu and a given evaluation is x, the squared deviation is (mu - x)^2.

3. Compute the sum of all squared deviations from step 2. This sum is the badness.

Compute the minimum badness over all possible collections of scores that can be obtained.
