#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size;
    cin >> size;
    vector<int>data;
    int i = 0;
    int element;
    while(i++<size)
    {
        cin >> element;
        data.push_back(element);
    }
    sort(data.begin(),data.end());
    for(auto x : data)
        cout << x << " ";
    
    return 0;
}
