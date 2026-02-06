/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  var map = Object.create(null);
  var result = [];
  for (var num1 of nums1) {
    var count = map[num1] || 0;
    map[num1] = count + 1;
  }

  for (var num2 of nums2) {
    var count = map[num2];
    if (!count) {
      continue;
    }
    result.push(num2);
    map[num2] = count - 1;
  }

  return result;
};
