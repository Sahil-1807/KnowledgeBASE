#include <bits/stdc++.h> 
using namespace std;
#define MAX=501
int getId(int M[MAX][MAX], int n);
int main()
{
    int MATRIX[4][4] = {{0, 0, 1, 0}, 
                    {0, 0, 1, 0}, 
                    {0, 0, 0, 0}, 
                    {0, 0, 1, 0}};
    cout<<getId(MATRIX,4)<<endl;
}
int getId(M[MAX][MAX],n)
{
    stack<int> s;
    for(int i=0;i<n;i++) s.push(i);
    int A,B,C;
    A = s.top();
    s.pop();
    B = s.top();
    s.pop();
    
    while(s.size()>1)
    {
        if(M[A][B]) A = s.top();
        else B = s.top();
        s.pop();
    }
    
    C = s.top();
    
    if(M[C][A]) C = A;
    if(M[C][B]) C = B;
    
    for(int i=0;i<n;i++)
    {
        if(M[C][i]||(!M[i][C])) return -1;
    }
    return C;
}