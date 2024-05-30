// const nums = [
//     20,
//     51,
//     3,
//     801,
//     415,
//     62,
//     4,
//     17,
//     19,
//     11,
//     1,
//     100,
//     1244,
//     104,
//     944,
//     854,
//     34,
//     3000,
//     3001,
//     1200,
//     633
//   ];

function radixSort(array) {
    // find the longest number
    const longestNumber = getLongestNumber(array);
  
    // create needed buckets  
    // an array of 10 arrays
    const buckets = new Array(10).fill().map(() => []);
  
    for (let i = longestNumber - 1; i >= 0; i--) {
      while (array.length) {
        const current = array.shift()
        buckets[getDigit(current, i, longestNumber)].push(current);
      }
  
      for (let j = 0; j < 10; j++) {
        while (buckets[j].length) {
          array.push(buckets[j].shift());
        }
      }
    }
  
    return array;
  }