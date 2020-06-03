#include <iostream>
using namespace std;

#define M (unsigned long long)((1e9)+7)

unsigned long long bf(unsigned long long a, unsigned long long b) {
  int r = 1;
  for (int i=0; i<b; i++) {
    r = (r*a)%M;
  }
  return r;
}

int main(int arg, char** argv)
{
    unsigned long long n, a, b;
    cin>>n;

    for (unsigned long long i=0; i<n; i++) {
      cin>>a>>b;
      cout<<bf(a, b)<<endl;
    }
    return 0;
}