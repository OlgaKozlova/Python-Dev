var isValid = function (char) {
  return /[0-9a-zA-Z]/.test(char);
};
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  var start = 0;
  var end = s.length - 1;
  while (start < end) {
    var started = s[start];
    var ended = s[end];
    while (start < end && !isValid(started)) {
      start++;
      started = s[start];
    }
    while (start < end && !isValid(ended)) {
      end--;
      ended = s[end];
    }
    if (started.toLowerCase() !== ended.toLowerCase()) {
      return false;
    }
    start++;
    end--;
  }

  return true;
};
