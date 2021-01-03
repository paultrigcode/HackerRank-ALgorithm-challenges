function birthdayCakeCandles(arr) {
    // Step 1
    let max = 0;
    let counter = 0;

    // Step 2 (a)
    arr.forEach(item => {
        // Step 3
        if (item > max) {
            // Step 4
            max = item;
            counter = 1;
            // Step 2 (b)
        } else if (item === max) {
            counter++;
        }
    });

    return counter;
}

console.log(birthdayCakeCandles([3,4,5,5]));