#include <iostream>
using namespace std;

struct Vec
{
  long long x, y;
  Vec() = default;
  Vec(long long _x, long long _y) : x(_x), y(_y) {}

  Vec operator-(const Vec &other) const
  {
    return {x - other.x, y - other.y};
  }
};

long long
cross(const Vec &a, const Vec &b)
{
  return a.x * b.y - a.y * b.x;
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  Vec p[3];
  for (auto &v : p)
    cin >> v.x >> v.y;

  Vec a = p[1] - p[0];
  Vec b = p[2] - p[0];

  long long z = cross(a, b);
  cout << (z > 0 ? 1 : z < 0 ? -1
                             : 0)
       << '\n';
}