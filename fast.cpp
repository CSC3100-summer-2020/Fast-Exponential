#include <iostream>
using namespace std;

#define M (unsigned long long)((1e9) + 7)

unsigned long long fast(unsigned long long a, unsigned long long b)
{
  unsigned long long r = 1, c = a;
  while (b > 0)
  {
    if (b & 1 == 1)
    {
      r = (r * c) % M;
    }
    b = b >> 1;
    c = (c * c) % M;
  }
  return r;
}

int main(int argc, char** argv)
{
  unsigned long long n, a, b;
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> a >> b;
    cout << fast(a, b) << endl;
  }
  return 0;
}