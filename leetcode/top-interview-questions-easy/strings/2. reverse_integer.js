/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  var isNegative = x < 0;
  var string = String(x);

  if (isNegative) {
    string = string.slice(1);
  }

  arr = string.split("");
  arr.reverse();
  string = arr.join("");

  // Убираем ведущие нули
  string = string.replace(/^([0]*)/, "");

  if (string.length > 10) {
    return 0;
  }

  if (string.length === 10) {
    var compare = isNegative ? "2147483648" : "2147483647";

    if (string > compare) {
      return 0;
    }
  }

  return Number(string) * (isNegative ? -1 : 1);
};
