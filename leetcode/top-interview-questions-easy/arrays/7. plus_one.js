/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  var shouldIncreasePrevious = false;
  var resultArray = [];
  for (var i = digits.length - 1; i >= 0; i--) {
    var shouldAddOne = i === digits.length - 1 || shouldIncreasePrevious;
    var current = digits[i];
    var result = shouldAddOne ? current + 1 : current;
    var digitResult = result % 10;

    resultArray.unshift(digitResult);

    shouldIncreasePrevious = result > 9;
    //console.log(i, digits[i], result, digitResult, shouldIncreasePrevious, resultArray);
  }

  if (shouldIncreasePrevious) {
    resultArray.unshift(1);
  }

  return resultArray;
};
