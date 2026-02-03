/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }

  var map = {};
  for (var char of s) {
    const count = map[char] || 0;
    map[char] = count + 1;
  }

  for (var char of t) {
    const count = map[char] || 0;
    map[char] = count - 1;
  }

  for (var key of Object.values(map)) {
    if (key !== 0) {
      return false;
    }
  }

  return true;
};
