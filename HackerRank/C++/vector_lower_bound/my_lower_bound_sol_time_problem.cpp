#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size,element;
    cin >> size;
    vector<int>data;
    for(int i = 0;i<size;i++)
    {
        cin >> element;
        data.push_back(element);
    }
    int queries;
    cin >> queries;
    for(int i = 0;i<queries;i++)
    {
        cin >> element;
        auto t = find(data.begin(),data.end(),element);
        if(t != data.end())
            cout << "Yes " << t-data.begin()+1 << endl;
        else if(t == data.end())
        {
            cout << "No ";
            auto it = lower_bound(data.begin(), data.end(), element);
            cout << it-data.begin()+1 << endl;
        }
    }
    
    return 0;
}