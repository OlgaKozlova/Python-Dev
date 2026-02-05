/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  var startParsing = false;
  var isNegative = false;
  var limit = 2 ** 31;
  var min = -1 * limit;
  var max = limit - 1;

  var space = " ";
  var plus = "+";
  var minus = "-";
  var zero = "0";
  var nine = "9";

  var result = 0;

  for (var char of s) {
    if (char === space) {
      if (!startParsing) {
        continue;
      } else {
        break;
      }
    }

    if (char === plus || char === minus) {
      if (!startParsing) {
        startParsing = true;
        if (char === minus) {
          isNegative = true;
        }
        continue;
      } else {
        break;
      }
    }

    if (char >= zero && char <= nine) {
      var number = char.charCodeAt(0) - zero.charCodeAt(0);
      startParsing = true;
      result = result * 10;
      result += number;

      if (isNegative) {
        if (result * -1 < min) {
          return min;
        }
      } else {
        if (result > max) {
          return max;
        }
      }
    } else {
      break;
    }
  }

  return isNegative ? result * -1 : result;
};
