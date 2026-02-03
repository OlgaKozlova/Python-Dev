/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function (s) {
  var len = s.length;
  for (let i = 0; i < len / 2; i++) {
    let lastIndex = len - i - 1;
    let first = s[i];
    let last = s[lastIndex];
    s[i] = last;
    s[lastIndex] = first;
  }
};
