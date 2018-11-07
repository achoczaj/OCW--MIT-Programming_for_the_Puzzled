//MIT 6.S095 - Programming for the Puzzled - Srini Devadas
/*
Puzzle 1 - You Will All Conform
Input is a vector of F's and B's, in terms of forwards and backwards caps.
Output is a set of commands (printed out) to get either all F's or all B's.
Fewest commands are the goal.
*/

//@ts-check

/**
 * pleaseConform Version 1
 * @param {string} caps - list of caps "F" (forward cap) or "B" (backward cap)
 */

 // Create an associative array with intervals {start: [index], end: [index], type: ["F" or "B"]}
 export const pleaseConformV1 = caps => {
  let start = 0;
  let forward = 0;
  let backward = 0;
  const intervals = [];

  for (let i = 0; i < caps.length; i++) {
    if (caps[i] != caps[start]) {
      intervals.push({ start: start, end: i - 1, type: caps[start] });

      if (caps[start] === "F") {
        forward++;
      } else {
        backward++;
      }
      start = i;
    }
  }
  intervals.push({ start: start, end: caps.length - 1, type: caps[start] });

  // Count forward and backward intervals
  if (caps[start] === "F") {
    forward++;
  } else {
    backward++;
  }

  // Choose flip option
  let flip = forward < backward ? "F" : "B";
  return intervals.filter(interval => interval.type === flip);
};

/**
  * * pleaseConform Version 2
  * @param {string} caps - list of caps "F" (forward cap) or "B" (backward cap)
 */
export const pleaseConformV2 = caps => {
  let start = 0;
  let forward = 0;
  let backward = 0;
  const intervals = [];

  caps = [...caps, "END"];

  for (let i = 0; i < caps.length; i++) {
    if (caps[i] != caps[start]) {
      intervals.push({ start: start, end: i - 1, type: caps[start] });
      // Count forward and backward intervals
      if (caps[start] === "F") {
        forward++;
      } else {
        backward++;
      }
      start = i;
    }
  }
  // Choose flip option
  let flip = forward < backward ? "F" : "B";
  return intervals.filter(interval => interval.type === flip);
};

/**
* pleaseConform - only one pass by caps vector
* @param {string} caps - list of caps "F" (forward cap) or "B" (backward cap)
 */
export const pleaseConformOnePass = caps => {
  caps = [...caps, caps[0]];
  const intervals = [];
  let start = 0;
  for (let i = 1; i < caps.length; i++) {
    if (caps[i] != caps[i - 1]) {
      if (caps[i] != caps[0]) {
        start = i;
      } else {
        intervals.push({ start: start, end: i - 1, type: caps[i - 1] });
      }
    }
  }
  return intervals;
};
