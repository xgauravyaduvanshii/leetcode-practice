// 2726. Calculator with Method Chaining (Easy)
// https://leetcode.com/problems/calculator-with-method-chaining/
// Submission 2200149764 -- Accepted, JavaScript
// My thinking: keep a running result and return this from every
// operation so calls chain; division by zero is the one error.
class Calculator {
    constructor(value) {
        this.result = value;
    }

    add(value) {
        this.result += value;
        return this;
    }

    subtract(value) {
        this.result -= value;
        return this;
    }

    multiply(value) {
        this.result *= value;
        return this;
    }

    divide(value) {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }
        this.result /= value;
        return this;
    }

    power(value) {
        this.result **= value;
        return this;
    }

    getResult() {
        return this.result;
    }
}
