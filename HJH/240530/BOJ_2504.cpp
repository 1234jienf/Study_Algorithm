#include <iostream>
#include <vector>
#include <string.h>

using namespace std;
typedef long long ll;

int main() {
	string line;
	vector<bool> round;
	ll sums[16];
	memset(sums, 0, 16 * sizeof(ll));
	cin >> line;
	ll score = 1;
	int depth = 0;
	for (char letter : line) {
		if (letter == '(') {
			round.push_back(true);
			if (score != 1) {
				sums[depth] += score;
			}
			depth++;
		}
		else if (letter == '[') {
			round.push_back(false);
			if (score != 1) {
				sums[depth] += score;
			}
			depth++;
		}
		else if (letter == ')') {
			if (round.size() == 0 || round.back() != true) {
				cout << 0;
				return 0;
			}
			round.pop_back();
			if (sums[depth] == 0) {
				sums[depth] = 1;
			}
			sums[depth - 1] += sums[depth] * 2;
			sums[depth--] = 0;
		}
		else if (letter == ']') {
			if (round.size() == 0 || round.back() != false) {
				cout << 0;
				return 0;
			}
			round.pop_back();
			if (sums[depth] == 0) {
				sums[depth] = 1;
			}
			sums[depth - 1] += sums[depth] * 3;
			sums[depth--] = 0;
		}
	}
	if (round.size() != 0) {
		cout << 0;
		return 0;
	}

	cout << sums[0];
}
