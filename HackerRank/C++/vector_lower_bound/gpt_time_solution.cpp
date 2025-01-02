#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int size, element;
    cin >> size;

    vector<int> data(size);
    for (int i = 0; i < size; i++)
        cin >> data[i];
    
    sort(data.begin(), data.end());

    int queries;
    cin >> queries;

    for (int i = 0; i < queries; i++)
    {
        cin >> element;

        auto it = lower_bound(data.begin(), data.end(), element);

        if (it != data.end() && *it == element)
            cout << "Yes " << (it - data.begin() + 1) << endl;
        else
            cout << "No " << (it - data.begin() + 1) << endl;
    }

    return 0;
}
