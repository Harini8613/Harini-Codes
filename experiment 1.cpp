#include <iostream>
using namespace std;
class student
{
    private:
       int rollno;
       string name;
    public:
    Student(int r,string n)
    {
        rollno=r;
        name=n;
        cout<<"student object created"<<endl;
    }
    void display(){
        cout<<"roll no="<<rollno<<endl;
        cout<<"name="<<name<<endl;
    }
    ~Student()
    {
        cout<<"student object destroyed"<<endl;
    }
};

int main() {
    Student s1(101,"Arun");
    s1.display();

    return 0;
}