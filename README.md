# pyRndSetPartitionGenerator

Generation of a Random Partition of a Finite Set by an Urn Model

## Usefull information:

- https://www.sciencedirect.com/science/article/pii/0097316583900092
- https://en.wikipedia.org/wiki/Bell_number#Moments_of_probability_distributions
- https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Recurrence_relation

## Usage
```
./main.py N Q
```
N: set size
K: number of random set partitions to generate

### Example
```
./main.py 10 100
```
Generate 100 random partitions of size 10 sets

## Applications
- The code can be easily modified to compute Stirling numbers of the second kind for a given set size N
- The built in Bell number function can compute Bell Numbers for big N's
- Given that this algorithm generates random set partitions with the correct natural distribution it can be used with the [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method) to get very accurate statistics related to set partitions

## Recommendations
- If speed is needed and N is big, you can pre-compute the needed Bell Numbers, save them into a file and use that instead of the built in Bell number function.
- The same cache trick can be applied for the Unm function, although m can be infinite, the probability of big a m appearing converges to 0, computing it up to 2*N should be more than enogh



Please report any issues and suggestions. Thank you
