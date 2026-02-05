/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let map = {};
  for (num of nums) {
    if (map[num]) {
      return true;
    } else {
      map[num] = true;
    }
  }
  return false;
};
