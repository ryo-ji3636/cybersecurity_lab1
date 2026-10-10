#include <iostream>
using namespace std;

int* getPointer() {
    int x = 100;
    return &x;
}

int main() {
    int* p = getPointer();

    cout << *p << endl;

    return 0;
}
