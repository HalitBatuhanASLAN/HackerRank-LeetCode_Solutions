#include <iostream>
#include <string>

using namespace std;

class Student
{
    public:
        void set_age(int input_age)
        {
            age = input_age;
        }
        void set_first_name(string name)
        {
            first_name = name;
        }
        void set_last_name(string surname)
        {
            last_name = surname;
        }
        void set_standard(int input_standard)
        {
            standard = input_standard;
        }

        int get_age()
        {
            return age;
        }
        string get_first_name()
        {
            return first_name;
        }
        string get_last_name()
        {
            return last_name;
        }
        int get_standard()
        {
            return standard;
        }

        string to_string()
        {
            string return_string = (std::to_string(age) + "," + first_name + "," + last_name + "," + std::to_string(standard));
            return return_string;
        }

    private:
        int age,standard;
        string first_name,last_name;
};

int main() {
    int age, standard;
    string first_name, last_name;

    cin >> age >> first_name >> last_name >> standard;

    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);

    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();

    return 0;
}
