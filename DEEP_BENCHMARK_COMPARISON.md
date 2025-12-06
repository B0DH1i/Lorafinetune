# 🎯 Benchmark Sonuçları Karşılaştırması
## Model: Qwen2.5-Coder-1.5B-Instruct + LoRA
**Dataset:** DEEP-5K (Solution Only Training)
**LoRA Config:** r=32, alpha=64, dropout=0.15
**Training:** 3 epochs, lr=3e-5, batch=16
---
## 📊 Özet Karşılaştırma
| Checkpoint | Doğru Sayısı | Accuracy | Ortalama Benzerlik |
|------------|--------------|----------|--------------------|
| checkpoint-400 | 1/8 | 12.5% | 38.9% |
| checkpoint-600 | 1/8 | 12.5% | 42.4% |
| checkpoint-700 | 2/8 | 25.0% | 37.8% |

---
## 📝 Soru Bazında Detaylı Karşılaştırma

### Soru 1
**Difficulty:** 1
**Question ID:** `fcf99ebf3819b88c184bd49e190ed83c`

#### ✅ Beklenen Çözüm
```python
def main():
    N = int(input().strip())
    sheets = (N + 1) // 2
    print(sheets)

if __name__ == "__main__":
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ⚠️ Orta (Benzerlik: 63.9%)
```python
def main():
    n = int(input().strip())
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    else:
        # If even: ceil(n/2) sheets
        # If odd: ceil((n+1)/2) sheets
        import math
        print(math.ceil((n + 1) / 2))

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ⚠️ Orta (Benzerlik: 69.7%)
```python
def main():
    n = int(input().strip())
    
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        print((n + 1) // 2)

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ✓ İyi (Benzerlik: 82.7%)
```python
def main():
    n = int(input().strip())
    print((n + 1) // 2)

if __name__ == '__main__':
    main()
```

---

### Soru 2
**Difficulty:** 2
**Question ID:** `d8b1674309875fa03c6115c1653d0ae9`

#### ✅ Beklenen Çözüm
```python
def main():
    a, b = input().split()
    reversed_a = int(a[::-1])
    reversed_b = int(b[::-1])
    print(max(reversed_a, reversed_b))

if __name__ == "__main__":
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ❌ Zayıf (Benzerlik: 40.5%)
```python
def main():
    A, B = map(int, input().split())
    
    # Convert numbers to strings for easy comparison
    str_A = str(A)
    str_B = str(B)
    
    # Compare from right to left (most significant digits)
    i = len(str_A) - 1
    j = len(str_B) - 1
    
    while i >= 0 and j >= 0:
        if str_A[i] > str_B[j]:
            print(str_A[i:])
            return
        elif str_A[i] < str_B[j]:
            print(str_B[j:])
            return
        else:
            i -= 1
            j -= 1
            
    # If all digits match so far, compare lengths
    if len(str_A) > len(str_B):
        print(str_A)
    else:
        print(str_B)

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ⚠️ Orta (Benzerlik: 64.5%)
```python
def main():
    A, B = map(int, input().split())
    
    # Convert to strings for easier manipulation
    str_A = str(A)
    str_B = str(B)
    
    # Reverse both numbers
    rev_A = int(str_A[::-1])
    rev_B = int(str_B[::-1])
    
    # Compare reversed versions
    if rev_A > rev_B:
        print(rev_A)
    else:
        print(rev_B)

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ⚠️ Orta (Benzerlik: 61.8%)
```python
def main():
    A, B = map(int, input().split())
    
    # Convert to strings for easy manipulation
    str_A = str(A)
    str_B = str(B)
    
    # Reverse each string using slicing
    rev_A = str_A[::-1]
    rev_B = str_B[::-1]
    
    # Compare the reversed strings
    if rev_A > rev_B:
        print(rev_A)
    else:
        print(rev_B)

if __name__ == "__main__":
    main()
```

---

### Soru 3
**Difficulty:** 3
**Question ID:** `8351892629419114301d3bf25ad5dac2`

#### ✅ Beklenen Çözüm
```python
def main():
    N = int(input().strip())
    
    # Get number of digits in N
    d = len(str(N))
    
    count = 0
    
    # Count numbers with odd digit counts less than d
    for k in range(1, d, 2):
        count += 9 * (10 ** (k - 1))
    
    # If current digit count is odd, add numbers with exactly d digits that are <= N
    if d % 2 == 1:
        count += N - (10 ** (d - 1)) + 1
    
    print(count)

if __name__ == "__main__":
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ❌ Zayıf (Benzerlik: 59.1%)
```python
def main():
    n = int(input().strip())
    
    # Count numbers with odd digit count
    count_odd = 0
    
    for i in range(1, n + 1):
        str_num = str(i)
        if len(str_num) % 2 != 0:
            count_odd += 1
            
    print(count_odd)

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ❌ Zayıf (Benzerlik: 59.1%)
```python
def main():
    N = int(input().strip())
    result = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            result += 1
    print(result)

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ❌ Zayıf (Benzerlik: 15.5%)
```python
def main():
    n = int(input().strip())
    
    if n == 0:
        print(0)
        return
        
    # Calculate number of digits for each power of 10
    digit_counts = []
    current_power = 1
    while True:
        count = (n + current_power - 1) // current_power
        digit_counts.append(count)
        if current_power * 10 > n:
            break
        current_power *= 10
    
    total_digits = sum(digit_counts)
    result = total_digits - (digit_counts[0] + digit_counts[-1])
    print(result)

if __name__ == '__main__':
    main()
```

---

### Soru 4
**Difficulty:** 4
**Question ID:** `f593a573836cb716fb0ba391eb24a6d3`

#### ✅ Beklenen Çözüm
```python
def main():
    import sys
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    bulbs = []
    idx = 2
    for _ in range(m):
        k = int(data[idx])
        idx += 1
        switches = list(map(int, data[idx:idx+k]))
        idx += k
        bulbs.append(switches)
    
    p_list = list(map(int, data[idx:idx+m]))
    idx += m
    
    count = 0
    for mask in range(1 << n):
        valid = True
        for i in range(m):
            connected_switches = bulbs[i]
            on_count = 0
            for switch in connected_switches:
                switch_index = switch - 1
                if mask & (1 << switch_index):
                    on_count += 1
            if on_count % 2 != p_list[i]:
                valid = False
                break
        if valid:
            count += 1
            
    print(count)

if __name__ == "__main__":
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ❌ Zayıf (Benzerlik: 25.4%)
```python
def main():
    import sys
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Parse k_i for each bulb
    k = []
    index = 2
    for _ in range(m):
        k.append(int(data[index]))
        index += 1
    
    # Parse p_i for each bulb
    p = []
    for i in range(m):
        p.append(int(data[index + i]))
    
    # Precompute factorials up to max(k_i) for efficient combination calculation
    max_k = max(k)
    fact = [1] * (max_k + 1)
    inv_fact = [1] * (max_k + 1)
    
    for i in range(2, max_k + 1):
        fact[i] = fact[i-1] * i % (10**9 + 7)
    
    inv_fact[max_k] = pow(fact[max_k], 10**9 + 7 - 2, 10**9 + 7)
    for i in range(max_k, 1, -1):
        inv_fact[i-1] = inv_fact[i] * i % (10**9 + 7)
    
    def binomial(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * inv_fact[r] % (10**9 + 7) * inv_fact[n-r] % (10**9 + 7)
    
    total = 0
    for bitmask in range(1 << n):
        count_on = 0
        for i in range(n):
            if bitmask & (1 << i):
                count_on += 1
        
        # Check if current state lights all bulbs
        valid = True
        for j in range(m):
            mask_bulb = 0
            for s_idx in range(k[j]):
                mask_bulb |= (bitmask >> (s_idx - 1)) & 1
            
            if (count_on + (mask_bulb & 1)) % 2 != p[j]:
                valid = False
                break
        
        if valid:
            total = (total + 1) % (10**9 + 7)
    
    print(total)

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ❌ Zayıf (Benzerlik: 34.3%)
```python
def main():
    import sys
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    connections = []
    for _ in range(m):
        k = int(data[index]); index += 1
        row = [int(x) for x in data[index:index+k]]
        index += k
        connections.append(row)
    
    p_values = [int(data[index + i]) for i in range(m)]
    
    # Create adjacency list for graph
    graph = [[] for _ in range(n+1)]
    for u, v_list in enumerate(connections):
        for v in v_list:
            if u < v:
                graph[u].append(v)
    
    # DP: dp[mask] = count of valid configurations with mask on
    dp = [0] * (1 << n)
    dp[0] = 1
    
    for mask in range(1 << n):
        # Check each bulb
        valid = True
        for bulb in range(m):
            current_count = sum((mask >> (u-1)) & 1 for u in connections[bulb])
            if (current_count % 2 != p_values[bulb]):
                valid = False
                break
        
        if valid:
            for neighbor in graph[mask]:
                dp[mask | neighbor] += dp[mask]
    
    result = dp[(1 << n) - 1]
    print(result)

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ❌ Zayıf (Benzerlik: 25.3%)
```python
def main():
    import sys
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Parse switch bulb connections
    k = [int(data[i]) for i in range(2, 2 + m)]
    switch_bulbs = []
    idx = 2 + m
    for i in range(m):
        s = []
        for j in range(k[i]):
            index = idx + j * 2
            s.append(int(data[index]))
        switch_bulbs.append(s)
        idx += k[i] * 2
    
    # Parse query conditions
    queries = []
    idx = idx + m
    for i in range(idx, idx + m):
        queries.append(int(data[i]))
    
    # Generate all binary strings for switches
    total_switches = (1 << n)
    valid_count = 0
    
    for mask in range(total_switches):
        # Check if this configuration satisfies all conditions
        all_conditions_met = True
        
        for bulb_idx in range(m):
            bulb_condition = queries[bulb_idx]
            bulb_bulbs = switch_bulbs[bulb_idx]
            
            # Count how many switches are on for this bulb
            count_on = 0
            for bulb in bulb_bulbs:
                if (mask >> (bulb - 1)) & 1:
                    count_on += 1
            
            # Check if condition is met
            if (count_on % 2) != bulb_condition:
                all_conditions_met = False
                break
                
        if all_conditions_met:
            valid_count += 1
            
    print(valid_count)

if __name__ == "__main__":
    main()
```

---

### Soru 5
**Difficulty:** 5
**Question ID:** `c3bd27ed3ada9eb872c9a9d6734e77bb`

#### ✅ Beklenen Çözüm
```python
def main():
    A1, A2, A3 = map(int, input().split())
    total = A1 + A2 + A3
    if total >= 22:
        print("bust")
    else:
        print("win")

if __name__ == "__main__":
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ✓ İyi (Benzerlik: 89.6%)
```python
def main():
    A = list(map(int, input().split()))
    total = sum(A)
    if total >= 22:
        print("bust")
    else:
        print("win")

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ✓ İyi (Benzerlik: 89.6%)
```python
def main():
    A = list(map(int, input().split()))
    total = sum(A)
    if total >= 22:
        print("bust")
    else:
        print("win")

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ✓ İyi (Benzerlik: 89.6%)
```python
def main():
    A = list(map(int, input().split()))
    total = sum(A)
    if total >= 22:
        print("bust")
    else:
        print("win")

if __name__ == "__main__":
    main()
```

---

### Soru 6
**Difficulty:** 6
**Question ID:** `0d0a11bf7b560f7c854a080cc1c5c31e`

#### ✅ Beklenen Çözüm
```python
def main():
    n_str = input().strip()
    if n_str == '0':
        print(0)
        return
        
    state0 = 0
    state1 = float('inf')
    
    for char in n_str:
        d = int(char)
        new_state0 = min(state0 + d, state1 + (d + 1))
        new_state1 = min(state0 + (10 - d), state1 + (9 - d))
        state0, state1 = new_state0, new_state1
        
    print(state0)

if __name__ == '__main__':
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ❌ Zayıf (Benzerlik: 12.6%)
```python
def main():
    n = int(input().strip())
    
    # Precompute Fibonacci numbers up to n
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    count = 0
    index = n
    
    while index > 0:
        count += 1
        index -= fib[index]
    
    print(count)

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ❌ Zayıf (Benzerlik: 11.7%)
```python
def main():
    n = int(input().strip())
    
    if n == 0:
        print(0)
        return
        
    # Precompute powers of 2 up to 10^9
    max_power_of_2 = 1 << 30  # 10^9 + 1
    powers_of_2 = [1] * (max_power_of_2.bit_length() + 1)
    for i in range(1, len(powers_of_2)):
        powers_of_2[i] = powers_of_2[i-1] * 2
    
    result = float('inf')
    
    # Try each power of 2 up to 10^9
    for k in range(max_power_of_2):
        if k > n:
            continue
            
        # Calculate number of coins needed to give change using k
        remaining = n - k
        count = 0
        idx = k.bit_length()
        
        while idx <= remaining.bit_length():
            # Find position where we need to split
            bit_position = remaining.bit_length() - idx
            mask = (1 << (bit_position + 1)) - 1
            low_part = remaining & mask
            high_part = remaining >> (bit_position + 1)
            
            # Add high part
            count += high_part
            
            # If low part is zero, done
            if low_part == 0:
                break
                
            # Add low part coins
            idx = low_part.bit_length()
            mask = (1 << idx) - 1
            low_high_pair = low_part | (high_part << idx)
            
            # Find corresponding coin
            # First find index of most significant 1 bit in low_high_pair
            # Then add 1 to get the actual value
            msb_index = low_high_pair.bit_length() - 1
            coin_value = 1 << (msb_index + 1)
            
            # Subtract the coin value from low_high_pair
            # The rest should fit into lower bits
            remaining -= coin_value
            count += 1
            
        result = min(result, count)
    
    print(result)

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ❌ Zayıf (Benzerlik: 8.0%)
```python
def main():
    n = int(input().strip())
    
    if n == 0:
        print(0)
        return
        
    # Precompute prime factors up to max possible value
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    factor_count = {}
    for p in primes:
        while n % p == 0:
            factor_count[p] = factor_count.get(p, 0) + 1
            n //= p
            
    min_exchanges = float('inf')
    
    # Try each combination of exponents for prime factors
    for exp_2 in range(factor_count.get(2, 0) + 1):
        for exp_3 in range(factor_count.get(3, 0) + 1):
            for exp_5 in range(factor_count.get(5, 0) + 1):
                for exp_7 in range(factor_count.get(7, 0) + 1):
                    for exp_11 in range(factor_count.get(11, 0) + 1):
                        for exp_13 in range(factor_count.get(13, 0) + 1):
                            for exp_17 in range(factor_count.get(17, 0) + 1):
                                for exp_19 in range(factor_count.get(19, 0) + 1):
                                    for exp_23 in range(factor_count.get(23, 0) + 1):
                                        for exp_29 in range(factor_count.get(29, 0) + 1):
                                            for exp_31 in range(factor_count.get(31, 0) + 1):
                                                for exp_37 in range(factor_count.get(37, 0) + 1):
                                                    for exp_41 in range(factor_count.get(41, 0) + 1):
                                                        for exp_43 in range(factor_count.get(43, 0) + 1):
                                                            for exp_47 in range(factor
```

---

### Soru 7
**Difficulty:** 7
**Question ID:** `9ef2281d89891a7cf3cf05e136888e04`

#### ✅ Beklenen Çözüm
```python
import math

def main():
    n, m, k = map(int, input().split())
    
    if m >= n:
        total_damage = n * (n + 1) // 2
    else:
        L = n - (m - 1)
        A = (L - 1 + k - 1) // k if L > 1 else 0
        S = m - 1
        
        phase1 = A * n - k * A * (A - 1) // 2
        phase2 = S * (n - A * k) - S * (S - 1) // 2
        phase3 = n - A * k - S
        
        total_damage = phase1 + phase2 + phase3
    
    print(total_damage)

if __name__ == '__main__':
    main()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ❌ Zayıf (Benzerlik: 14.0%)
```python
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    result = (n + m - 1) // m * k
    print(result)

if __name__ == "__main__":
    main()
```

**checkpoint-600** - ❌ Zayıf (Benzerlik: 5.8%)
```python
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    if m == 1:
        print(n)
        return
    
    # Calculate the sum of first m-1 positive numbers
    total_groups = m - 1
    max_damage_per_group = (total_groups * (total_groups + 1)) // 2
    
    # Check if we can reduce the total groups
    if max_damage_per_group > n:
        print(0)
        return
    
    result = n - max_damage_per_group
    print(result)

if __name__ == "__main__":
    main()
```

**checkpoint-700** - ❌ Zayıf (Benzerlik: 14.0%)
```python
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Calculate maximum damage per group
    max_damage_per_group = min(n // (m + 1) * (m + 1), n)
    
    # Total damage: n groups * max_damage_per_group - m groups * k
    result = (max_damage_per_group * m) - (m * k)
    print(result)

if __name__ == "__main__":
    main()
```

---

### Soru 8
**Difficulty:** 8
**Question ID:** `335a0ac185f9165175b2a6c5a3a92f74`

#### ✅ Beklenen Çözüm
```python
import sys
from collections import deque

def trace_light(grid, n, m, start_r, start_c, direction):
    # direction: 0=up, 1=right, 2=down, 3=left
    r, c = start_r, start_c
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    d = direction
    
    visited = set()
    
    while True:
        if (r, c, d) in visited:
            return None  # Cycle detected
        visited.add((r, c, d))
        
        # Move in current direction
        nr, nc = r + dr[d], c + dc[d]
        
        # Check boundaries
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            # Hit wall - reflect
            d = (d + 2) % 4
            continue
        
        cell = grid[nr][nc]
        
        if cell == '#':  # Obstacle
            return None
        
        if cell == '\\':
            # Mirror: 0->1, 1->0, 2->3, 3->2
            d = {0: 1, 1: 0, 2: 3, 3: 2}[d]
        elif cell == '/':
            # Mirror: 0->3, 1->2, 2->1, 3->0  
            d = {0: 3, 1: 2, 2: 1, 3: 0}[d]
        elif cell == 'V' or cell == 'H':
            # Found a gargoyle
            return (nr, nc, d)
        
        r, c = nr, nc

def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    gargoyles = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] in ['V', 'H']:
                gargoyles.append((i, j, grid[i][j]))
    
    if not gargoyles:
        print(0)
        return
    
    # For each gargoyle, check what each face can see in each orientation
    connections = []
    
    for idx, (r, c, typ) in enumerate(gargoyles):
        # Original orientation
        if typ == 'V':
            faces = [(0, 'up'), (2, 'down')]  # up and down
        else:  # 'H'
            faces = [(1, 'right'), (3, 'left')]  # right and left
            
        orig_connections = []
        for d, _ in faces:
            target = trace_light(grid, n, m, r, c, d)
            if target:
                tr, tc, td = target
                # Find which gargoyle this is
                for j, (gr, gc, gtyp) in enumerate(gargoyles):
                    if gr == tr and gc == tc:
                        # Check if the face direction matches the gargoyle type
                        if gtyp == 'V' and (td == 0 or td == 2):
                            orig_connections.append(j)
                        elif gtyp == 'H' and (td == 1 or td == 3):
                            orig_connections.append(j)
                        break
        
        # Rotated orientation
        if typ == 'V':
            rot_faces = [(1, 'right'), (3, 'left')]  # becomes H
        else:  # 'H'
            rot_faces = [(0, 'up'), (2, 'down')]  # becomes V
            
        rot_connections = []
        for d, _ in rot_faces:
            target = trace_light(grid, n, m, r, c, d)
            if target:
                tr, tc, td = target
                for j, (gr, gc, gtyp) in enumerate(gargoyles):
                    if gr == tr and gc == tc:
                        if gtyp == 'V' and (td == 0 or td == 2):
                            rot_connections.append(j)
                        elif gtyp == 'H' and (td == 1 or td == 3):
                            rot_connections.append(j)
                        break
        
        connections.append((orig_connections, rot_connections))
    
    # Simple greedy approach: try to satisfy each gargoyle
    rotated = [False] * len(gargoyles)
    satisfied = [False] * len(gargoyles)
    
    changed = True
    while changed:
        changed = False
        for i in range(len(gargoyles)):
            if satisfied[i]:
                continue
                
            orig_conn, rot_conn = connections[i]
            
            # Check if current orientation satisfies
            current_conn = rot_conn if rotated[i] else orig_conn
            if current_conn:
                satisfied[i] = True
                changed = True
            else:
                # Try rotating
                other_conn = orig_conn if rotated[i] else rot_conn
                if other_conn:
                    rotated[i] = not rotated[i]
                    satisfied[i] = True
                    changed = True
    
    # Check if all satisfied
    if all(satisfied):
        print(sum(rotated))
    else:
        print(-1)

if __name__ == "__main__":
    solve()
```

#### 🤖 Model Cevapları
**checkpoint-400** - ❌ Zayıf (Benzerlik: 5.8%)
```python
def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    if not data:
        print(-1)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, n + 1):
        grid.append(data[i].strip())
        
    # Parse the grid
    height = len(grid)
    width = len(grid[0])
    
    # Directions: up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    def find_gargoyles():
        gargoyles = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 'V':
                    gargoyles.append((i, j))
        return gargoyles
    
    def is_valid(x, y):
        return 0 <= x < height and 0 <= y < width and grid[x][y] != '#'
    
    def reflect(x, y, d):
        # Reflect along vertical axis
        if d == 0 or d == 2:
            return x, y
        elif d == 1:
            return x, width - 1 - y
        else:  # d == 3
            return height - 1 - x, y
    
    def rotate_and_count(gargoyles, count):
        visited = set()
        stack = [gargoyles]
        
        while stack:
            current = stack.pop()
            
            # Check if all faces are connected
            seen_faces = set()
            for x, y in current:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < height and 0 <= ny < width:
                        if grid[nx][ny] == 'V' and (nx, ny) in seen_faces:
                            continue
                        if grid[nx][ny] == '.':
                            continue
                        if (nx, ny) in visited:
                            continue
                        visited.add((nx, ny))
                        
                        # Check if we need to rotate
                        found_cycle = False
                        for dir_idx in range(4):
                            # Get original direction
                            orig_dir = (dir_idx + 2) % 4
                            
                            # Try reflecting
                            rx, ry = reflect(x, y
```

**checkpoint-600** - ❌ Zayıf (Benzerlik: 4.4%)
```python
import sys
from collections import deque

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(-1)
        return
        
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())
    
    # Precompute mirrored directions
    dir_map = {
        'N': 'S', 'S': 'N',
        'E': 'W', 'W': 'E'
    }
    
    # Directions relative to original orientation
    original_dirs = [
        ('N', 'N'), ('S', 'S'),
        ('E', 'W'), ('W', 'E')
    ]
    
    # Find all gargoyle positions
    gargoyle_positions = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'V' or grid[i][j] == 'H':
                gargoyle_positions.add((i, j))
    
    # Convert to tuple for hashing
    def pos_to_tuple(pos):
        return (pos[0], pos[1])
    
    # Check if two positions are connected via reflections
    def are_connected(p1, p2):
        if p1 == p2:
            return True
            
        # Original direction pair
        ori_dir1, ori_dir2 = original_dirs[p1]
        ori_dir2_rev = dir_map[ori_dir2]
        
        # Mirror directions
        mir_dir1 = ori_dir2_rev
        mir_dir2 = ori_dir1
        
        # Get current orientations
        curr_ori_dir1, curr_ori_dir2 = original_dirs[p2]
        curr_mir_dir1 = dir_map[curr_ori_dir2]
        curr_mir_dir2 = ori_dir1
        
        # BFS for each pair of orientations
        visited = set()
        queue = deque([(p1, p2)])
        
        while queue:
            u, v = queue.popleft()
            
            # Check if both positions are already visited with same orientation pair
            if (u, v, ori_dir1, ori_dir2) in visited:
                continue
                
            # Mark as visited
            visited.add((u, v, ori_dir1, ori_dir2))
            
            # Check if both orientations match
            if ori_dir1 == curr_ori_dir1 and ori_dir2 == curr_ori_dir2:
```

**checkpoint-700** - ❌ Zayıf (Benzerlik: 5.1%)
```python
from collections import deque
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, n + 1):
        grid.append(data[i].strip())
    
    # Find the starting position of the door
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.':
                start_i, start_j = i, j
                break
                
    # Directions: up, down, left, right
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def get_mirror_type(i, j):
        if grid[i][j] == '\\' or grid[i][j] == '/':
            return grid[i][j]
        else:
            return None
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] != '#'
    
    def get_gargoyles_in_range(start_i, start_j):
        visited = [[False] * m for _ in range(n)]
        q = deque()
        q.append((start_i, start_j))
        visited[start_i][start_j] = True
        
        gargoyles = set()
        
        while q:
            i, j = q.popleft()
            
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if is_valid(ni, nj):
                    if grid[ni][nj] == 'V' and not visited[ni][nj]:
                        q.append((ni, nj))
                        visited[ni][nj] = True
                        gargoyles.add((ni, nj))
                        
        return list(gargoyles)
    
    def count_rotations_to_connect(gargoyles):
        # Check connectivity using BFS
        visited = [[False] * m for _ in range(n)]
        parent = [[None] * m for _ in range(n)]
        
        # Start from one of the gargoyles
        start_pos = gargoyles[0]
        start_i, start_j = start_pos
        visited[start_i][start_j] = True
        parent[start_i][start_j] = start_pos
        
        # Perform BFS
        queue = deque([start_pos])
```

---

## 🏆 Sonuç
**En İyi Checkpoint:** checkpoint-700
- Accuracy: 25.0%
- Doğru Cevap: 2/8
- Ortalama Benzerlik: 37.8%
