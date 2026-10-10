#include <iostream>
using namespace std;

int main() {
    int* p = nullptr;

    cout << "Before dereference" << endl;
    cout << *p << endl;
    cout << "After dereference" << endl;

    return 0;
}
