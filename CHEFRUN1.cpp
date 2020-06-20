#include<iostream>
using namespace std;
int main()
{
  int t;
  cin>>t;
  while(t>0)
  {
  int x1, x2, x3, v1, v2;
  
  cin>>x1>>x2>>x3>>v1>>v2;
  float d1 , t1, d2, t2;
  
  d1= abs(x3-x1);
  d2= abs(x3-x2);
  t1 = d1/v1;
  t2 = d2/v2;
  
  if(d1==d2 && v1==v2)
  cout<<"Draw"<<endl;  
  
  if(t1<t2)
  cout<<"Chef"<<endl;
  
  if(t2<t1)
  cout<<"Kefa"<<endl;
  
  t--;
  }
  
  return 0;
  
  
}
