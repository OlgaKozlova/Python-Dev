/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  var prefix = strs[0];
  if (strs.length === 1) {
    return prefix;
  }

  for (var i = 1; i < strs.length; i++) {
    var current = strs[i];

    var newPrefix = "";
    for (var j = 0; j < current.length; j++) {
      if (current[j] === prefix[j]) {
        newPrefix += current[j];
      } else {
        break;
      }
    }

    if (newPrefix === "") {
      return newPrefix;
    }

    prefix = newPrefix;
  }

  return prefix;
};
