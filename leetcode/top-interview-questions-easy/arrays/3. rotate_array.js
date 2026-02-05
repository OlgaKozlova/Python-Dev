var reverse = function (nums, from, to) {
  var left = from;
  var right = to;
  while (left < right) {
    var tmp = nums[left];
    nums[left] = nums[right];
    nums[right] = tmp;
    left++;
    right--;
  }
};
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  var n = nums.length;
  k = k % n;
  if (k === 0) {
    return;
  }

  // Развернули весь массив
  reverse(nums, 0, n - 1);

  reverse(nums, 0, k - 1);

  reverse(nums, k, n - 1);
};
