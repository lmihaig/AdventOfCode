#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream input("day1.in");

int main()
{
    unsigned int x, i, j, m, size;
    vector<unsigned int> expense;
    while(input>>x)
    {
        expense.push_back(x);
    }

size = expense.size();

    for(i = 0; i < size; i++)
        for(j = i; j < size; j++)
            {
                if(expense[i]+expense[j] == 2020) 
                {
                    cout<<"Task1: "<<expense[i]*expense[j]<<'\n';
                }
            }

    for(i = 0; i < size; i++)
        for(j = i; j < size; j++)
            for(m = j; m < size; m++)
            {
                if(expense[i]+expense[j]+expense[m] == 2020) 
                {
                    cout<<"Task2: "<<expense[i]*expense[j]*expense[m]<<'\n';
                }
            }      
}