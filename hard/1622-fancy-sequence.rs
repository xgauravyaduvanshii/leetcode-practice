const MOD: i64 = 1_000_000_007;

struct Fancy {
    // My thinking: adding and multiplying everything at once
    // is lazy work — so remember the running add and multiply
    // and undo them only when a value is read out.
    nums: Vec<i64>,
    add: i64,
    mul: i64,
}

impl Fancy {
    fn new() -> Self {
        Fancy { nums: Vec::new(), add: 0, mul: 1 }
    }

    fn append(&mut self, val: i32) {
        let inv = mod_pow(self.mul, MOD - 2);
        self.nums.push(((val as i64 - self.add + MOD) % MOD) * inv % MOD);
    }

    fn add_all(&mut self, inc: i32) {
        self.add = (self.add + inc as i64) % MOD;
    }

    fn mult_all(&mut self, m: i32) {
        self.add = self.add * m as i64 % MOD;
        self.mul = self.mul * m as i64 % MOD;
    }

    fn get_index(&self, idx: i32) -> i32 {
        if idx as usize >= self.nums.len() {
            return -1;
        }
        ((self.nums[idx as usize] * self.mul + self.add) % MOD) as i32
    }
}

fn mod_pow(mut a: i64, mut e: i64) -> i64 {
    let mut res = 1i64;
    while e > 0 {
        if e & 1 == 1 {
            res = res * a % MOD;
        }
        a = a * a % MOD;
        e >>= 1;
    }
    res
}
