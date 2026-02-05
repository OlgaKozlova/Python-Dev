/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  var startIndex = 0;
  for (var i = 0; i < nums.length; i++) {
    if (nums[i] > nums[startIndex]) {
      startIndex++;
      nums[startIndex] = nums[i];
    }
  }

  return startIndex + 1;
};
