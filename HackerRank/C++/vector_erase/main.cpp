#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size,num;
    cin >> size;
    vector<int> data;
    for(int i = 0;i<size;i++)
    {
        cin >> num;
        data.push_back(num); 
    }
    int deleted_index;
    cin >> deleted_index;
    data.erase(data.begin() + deleted_index-1);
    int remove_first_index,remove_last_index;
    cin >> remove_first_index >> remove_last_index;
    for(int i = remove_first_index;i<remove_last_index;i++)
        data.erase(data.begin() + remove_first_index-1);
    cout << data.size() << endl;
    for(auto element:data)
        cout << element << " ";
            
    return 0;
}
