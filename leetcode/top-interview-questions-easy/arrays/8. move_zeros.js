/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  var notNullIndex = 0;
  for (var i = 0; i < nums.length; i++) {
    var current = nums[i];

    //console.log(nums, i, notNullIndex, current);

    if (current !== 0) {
      nums[i] = nums[notNullIndex];
      nums[notNullIndex] = current;
      notNullIndex++;
    }
  }
};
