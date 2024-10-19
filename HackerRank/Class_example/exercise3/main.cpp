#include<bits/stdc++.h>

using namespace std;

class Box
{
    public:
        Box(int l = 0,int b = 0,int h = 0):l(l),b(b),h(h){}
        Box(Box &another);

        int getLength();
        int getBreadth();
        int getHeight();
        long long CalculateVolume();
        
        friend ostream& operator<<(ostream& out, Box& B)
        {
            out << B.l << " " << B.b << " " << B.h;
            return out;
        }
        
        bool operator<(Box &another)
        {
            return (l < another.l ||
            (b<another.b && l == another.l) ||
            (h<another.h && l==another.l && b == another.b)
            );
        }
        
    private:
        int l, b, h;
};

Box::Box(Box &another)
{
    b = another.b;
    h = another.h;
    l = another.l;
}

int Box::getLength()
{
    return l;
}

int Box::getHeight()
{
    return h;
}

int Box::getBreadth()
{
    return b;
}

long long Box::CalculateVolume()
{
    long long volume = (long long)h*b*l;
    return volume;
}


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}