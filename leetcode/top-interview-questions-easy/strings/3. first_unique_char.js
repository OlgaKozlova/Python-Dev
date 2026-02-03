/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  var map = {};
  for (var i = 0; i < s.length; i++) {
    var char = s[i];
    var mapped = map[char] || { count: 0, index: i };
    mapped.count = mapped.count + 1;
    map[char] = mapped;
  }

  var filtered = Object.values(map).filter((item) => item.count === 1);
  if (filtered.length === 0) {
    return -1;
  }

  return filtered[0].index;
};
