/**
 * 풀이
 * - 탐색 방향을 90도씩 회전해나가면서 주어진 2차원 배열 matrix를 탐색합니다
 * - 한계: 주어진 matrix를 변형하게 되며, 해당 변형을 피하기 위해서는 추가적인 공간 사용이 필요합니다
 * 
 * Big O
 * - M: 주어진 matrix의 행의 개수
 * - N:               열의 개수
 * 
 * - Time complexity: O(MN)
 * - Space complexity: O(MN)
 */

class Solution {
public:
    pair<int, int> rotate(pair<int, int> dir) {
        // 시계방향 90도 회전
        // 행렬곱으로 구해줄 수 있습니다
        // | 0 -1 |  | dir.first   |  =  |  -dir.second  |
        // | 1  0 |  | dir.second  |     |   dir.first   |
        return {dir.second, -dir.first};
    }  

    pair<int, int> get_next(pair<int, int> curr, pair<int, int> dir) {
        return {curr.first + dir.first, curr.second + dir.second};
    }  

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int cnt = m * n;

        pair<int, int> curr = {0, 0};
        pair<int, int> curr_dir = {0, 1};

        vector<int> res;

        while (cnt) {
            res.push_back(matrix[curr.first][curr.second]);

            matrix[curr.first][curr.second] = 101; // constraint 밖의 값 101로 방문 여부를 표시합니다
            --cnt;
            
            pair<int, int> next = get_next(curr, curr_dir);

            if (0 > next.first || next.first >= m
                || 0 > next.second || next.second >= n
                || matrix[next.first][next.second] == 101) {
                curr_dir = rotate(curr_dir);
                curr = get_next(curr, curr_dir);
            } else {
                curr = next;
            }
        }

        return res;
    }
};

/**
 * 풀이
 * - 위와 동일하지만, 방문 여부를 기록하기 위해 m * n 크기의 정수형 2차원 배열 대신
 *   m 크기의 16비트 정수 배열을 사용합니다
 * - 더 이상 입력 배열을 변형하지 않습니다
 * - 공간복잡도가 개선되고 실제 공간 사용량도 줄어듭니다
 * 
 * Big O
 * - M: 주어진 matrix의 행의 개수
 * - N:               열의 개수
 * 
 * - Time complexity: O(MN)
 * - Space complexity: O(M)
 */

class Solution {
public:
    pair<int, int> rotate(pair<int, int> dir) {
        return {dir.second, -dir.first};
    }  

    pair<int, int> get_next(pair<int, int> curr, pair<int, int> dir) {
        return {curr.first + dir.first, curr.second + dir.second};
    }  

    void mark_visited(vector<uint16_t>& visit, pair<int, int> curr) {
        visit[curr.first] |= 1 << curr.second;
    }

    bool is_visited(vector<uint16_t> const visit, pair<int, int> curr) {
        return visit[curr.first] & 1 << curr.second;
    }

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int cnt = m * n;

        pair<int, int> curr = {0, 0};
        pair<int, int> curr_dir = {0, 1};

        vector<uint16_t> visit(m, 0);

        vector<int> res;

        while (cnt) {
            res.push_back(matrix[curr.first][curr.second]);

            mark_visited(visit, curr);
            --cnt;
            
            pair<int, int> next = get_next(curr, curr_dir);

            if (0 > next.first || next.first >= m
                || 0 > next.second || next.second >= n
                || is_visited(visit, next)) {
                curr_dir = rotate(curr_dir);
                curr = get_next(curr, curr_dir);
            } else {
                curr = next;
            }
        }

        return res;
    }
};
