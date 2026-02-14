/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  let accumulator = 0;
  for (var num of nums) {
    accumulator = accumulator ^ num;
  }

  return accumulator;
};
