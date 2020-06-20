#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int x1,x2,x3,v1,v2;
	    cin>>x1>>x2>>x3>>v1>>v2;
	    int d1,d2;
	    d1=x3-x1;
	    d2=x2-x3;
	    float t1=(float)d1/v1;
	    float t2=(float)d2/v2;
	    if(t1<t2)
	    {cout<<"Chef"<<endl;}
	    else if(t2<t1)
	    {cout<<"Kefa"<<endl;}
	    else if(t1==t2)
	    {cout<<"Draw"<<endl;}
	   
	}
	return 0;
}
