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
    vector<int>indexes;
    for(int i = 0;i<queries;i++)
    {
        cin >> element;
        auto t = find(data.begin(),data.end(),element);
        if(t != data.end())
            indexes.push_back(t-data.begin()+1);
        else if(t == data.end())
        {
            if(element > 0)
                element *= -1;
            else
                element = 0;
            indexes.push_back(element);
        }
    }
    for(int i = 0;i<indexes.size();i++)
    {
        if(indexes.at(i) > 0)
            cout << "Yes " << indexes.at(i) << endl;
        else
        {
            for(int j = 0;j<data.size();j++)
            {
                if(data.at(j) > indexes.at(i)*-1)
                {
                    cout << "No " << j+1 << endl;
                    break;
                }
            }
        }
    }
    return 0;
}
