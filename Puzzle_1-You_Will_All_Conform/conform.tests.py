# MIT 6.S095 - Programming for the Puzzled - Srini Devadas

# Puzzle 1 - You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps.
# Output is a set of commands (printed out) to get either all F's or all B's.
# Fewest commands are the goal.

# Tests for pleaseConform function

from ./conform.py import *

## TBD -> write tests in python

# more B intervals - should return caps array with B ", () => {
const caps1 = ["F", "F",
               "B", "B", "B",
               "F",
               "B", "B", "B",
               "F",  "F",
               "B",
               "F"  ];

const intervals = pleaseConform(caps1);
expect(intervals).toEqual([
  { start: 2, end: 4, type: "B" },
  { start: 6, end: 8, type: "B" },
  { start: 11, end: 11, type: "B" }
]);
});

# for caps1
# intervals [(0, 1, 'F'), (2, 4, 'B'), (5, 5, 'F'), (6, 8, 'B'), (9, 12, 'F')]


it("same number of F and B intervals - should return caps array with last interval type (B)", () => {
const caps2 = ["F", "F",
               "B", "B", "B",
               "F",
               "B", "B", "B",
               "F", "F",
               "B"];
const intervals = pleaseConform(caps2);
expect(intervals).toEqual([
  { start: 2, end: 4, type: "B" },
  { start: 6, end: 8, type: "B" },
  { start: 11, end: 11, type: "B" }
]);
});

it("only one interval (all caps the same, e.g. F) - should return empty array", () => {
const caps3 = ["F", "F"];
const intervals = pleaseConform(caps3);
expect(intervals).toEqual([]);
});

it("empty input - should return empty array ", () => {
const caps4 = [];
const intervals = pleaseConform(caps4);
expect(intervals).toEqual([]);
});
});
