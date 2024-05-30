// const nums = [10, 5, 3, 8, 2, 6, 4, 7, 9, 1];

const mergeSort = (nums) => {
    // base case, return if length 1 or 0
    if (nums.length < 2) {
      return nums;
    }
  
    // break into 2 smaller arrays
    const length = nums.length;
    const middle = Math.floor(length / 2);
    const left = nums.slice(0, middle);
    const right = nums.slice(middle);
  
    // call mergeSort() on left and right
    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);
    
    // return the merge of left and right
    return merge(sortedLeft, sortedRight);
  };
  
  const merge = (sortedLeft, sortedRight) => {
    const results = [];
  
    while(sortedLeft.length && sortedRight.length) {
      if (sortedLeft[0] <= sortedRight[0]) {
        results.push(sortedLeft.shift()); // consider alternative for better performance
      } else {
        results.push(sortedRight.shift()); // consider alternative for better performance
      }
    }
  
    // return one sorted array
    return results.concat(sortedLeft, sortedRight)
  }