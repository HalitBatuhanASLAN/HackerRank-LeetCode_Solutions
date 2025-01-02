#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person
{
    public:
        virtual void getdata() = 0;
        virtual void putdata() = 0;
        void setAge(int age){this->age = age;}
        void setName(string name){this->name = name;}
        string getName(){return name;}
        int getAge(){return age;}
    private:
        int age;
        string name;
};

class Professor : public Person
{
    public:
        //Professor(){cur_id++;}
        void getdata()
        {
            string tmp;
            int age_tmp;
            try {
                cin >> tmp >> age_tmp >> publications;
            } catch (...) {
                throw; 
            }
            setAge(age_tmp);
            setName(tmp); 
        }
        void putdata()
        {
            cout << getName() << " " << getAge() << " " << publications
             << " " << cur_id << endl;
             cur_id++;
        }
    private:
        int publications;
        static int cur_id;
};

class Student : public Person
{
    public:
        //Student(){cur_id++;}
        void getdata()
        {
            string tmp;
            int age_tmp;
            try {
                cin >> tmp >> age_tmp;
            } catch (...) {
                throw;
            }
            int i = 0;
            int grade = 0;
            while(i<6)
            {
                try{
                cin >> grade;}
                catch(...){throw;}
                tot_grade[i] = grade;
                i++;
            }
            setAge(age_tmp);
            setName(tmp); 
        }
        void putdata()
        {
            int grades = 0;
            for(int x : tot_grade) grades += x;
            cout << getName() << " " << getAge() << " " << grades
            << " " << cur_id << endl;
            cur_id++;
        }
    private:
        int tot_grade[6];
        static int cur_id;
};

int Professor::cur_id = 1;
int Student::cur_id = 1;

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
