"""TC: O(n), SC: O(1)

※ 코드를 보고 대충 뭘 했는지 감을 잡은 다음에 아래의 아이디어에서 p, n 구간이 나오는 부분만 보면
  좀 더 빠른 이해가 가능하다.

아이디어:
- 곱에 0이 섞이면 아무리 많은 수를 곱해도 결과는 0이다.
- 0이 등장하지 않는 어떤 subarray가 주어졌다고 하자.
    - 여기에 음수가 짝수 번 등장하면 모든 숫자를 곱한 것이 가장 큰 곱이 된다.
    - 음수가 홀수 번, 총 r번 등장한다고 해보자. 이 배열을 다음과 같이 구조화할 수 있다.
        - 양수를 p, 음수를 n이라고 표현하자.
        - 이 배열은 [p, ..., p, n, p, ... p, n, ..., n, p, ..., p] 꼴로 표현이 가능하다.
          이때, n은 총 r번 등장하고, n은 p가 여러 번(0번도 가능) 등장하는 묶음 사이에 존재한다.
        - p가 여러 번(0번도 가능) 등장하는 것을 P라고 묶어서 표현하면 아래와 같이 볼 수 있다.
        - [(P), n, (P), n, ..., n, (P), n, (P)]
        - n을 짝수 번 곱해야 양수가 나온다. 연속된 값을 최대한 많이 곱하려고 하므로, 한쪽 끝에
          등장하는 n을 뺀 나머지 n들을 곱하는 것이 가장 좋은 전략이다.
        - 위의 전략에 따라 배열의 숫자를 곱하려고 하면 다음 둘 중 하나가 가장 큰 숫자다.
            - [(P), n, (P), n, ..., n, (P), n, (P)]
                └───────────────────────┘
               이 구간의 숫자들을 모두 곱함
            - [(P), n, (P), n, ..., n, (P), n, (P)]
                        └───────────────────────┘
                       이 구간의 숫자들을 모두 곱함
        - 즉, 앞에서부터 숫자를 계속 곱하면서 max값을 찾은 것, 혹은 뒤에서부터 숫자를 계속
          곱하면서 max값을 찾은 것, 둘 중 하나가 위의 구간에서의 최대 곱셈 값이 된다.
- 우리에게 주어진 전체 array는 다음과 같이 표현 가능하다.
    - 0이 등장하지 않는 길이 1 이상의 subarray를 (S), 0으로만 이루어진 길이 0 이상의 subarray를
      (0)이라고 하면 아래와 같이 표현이 가능하다.
    - [(0), (S), (0), (S), ..., (S), (0), (S), (0)]
    - 전체 array에서 최대 subarray 곱은 0이거나, 혹은 위의 각 S에서의 최대 곱들 중 최대 값이다.
- 위의 아이디어를 활용하면 다음의 방식으로 최대 subarray의 곱을 찾을 수 있다.
    - nums의 앞에서부터 숫자를 하나씩 곱해가면서 최대 곱을 찾음. 단, 중간에 0이 나와서 최대 곱
      값이 0이 되었을 경우 이를 다시 1로 바꿔줘서 위의 아이디어를 적용할 수 있도록 세팅.
    - 똑같은 작업을 nums의 뒤에서부터 숫자를 하나씩 곱해가면서 진행함.


SC:
- solution을 저장하는 데에 O(1).
- 곱셈 값을 저장하는 데에 O(1).
- 총 O(1).

TC:
- 리스트를 앞에서부터 순회하면서 곱/max 연산. O(n).
- 리스트를 뒤에서부터 순회하면서 곱/max 연산. O(n).
- 총 O(n).
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sol = nums[0]
        p = 1
        for i in nums:
            if p == 0:
                p = 1
            p *= i
            sol = max(p, sol)
        p = 1
        for i in reversed(nums):
            if p == 0:
                p = 1
            p *= i
            sol = max(p, sol)
        return sol
