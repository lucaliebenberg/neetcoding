// const input = [10, 8, 2, 1, 6, 3, 9, 4, 7, 5];

function quickSort(nums) {
    if (nums.length <= 1){ // (length 0 | length 1)
      return nums;
    }
  
    const pivot = nums[nums.length - 1];
    // or
    // const pivot = nums.pop();
    // then can use ' for x in nums ' ( as pivot will not be included in nums )
  
    const left = [];
    const right = [];
  
    for (let i = 0; i < nums.length - 1; i++){ // NOTE: need to -1 from length, so 'pivot' is not included
      if (nums[i] < pivot){
        left.push(nums[i]);
      } else {
        right.push(nums[i])
      }
    }
  
    const sortedLeft = quickSort(left); // these are pointers
    const sortedRight = quickSort(right); // these are pointers
  
    return sortedLeft.concat(pivot, sortedRight);
    // return [...quickSort(left), pivot, ...quickSort(right)] // could do this for a 1 liner
  }