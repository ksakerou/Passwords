#include <iostream>
#include <string>
#include <ctime>
#include <cctype>
#include <algorithm>
using namespace std;
string alp(string alf){
	string A,alf2 = alf;
	for (int i=0;i<alf2.size();i++) {
		if (isupper(alf2[i])) alf2[i]=tolower(alf2[i]);
		else alf2[i]=toupper(alf2[i]);
	}
	alf += alf2;

	for (int i=0;i<alf.size();i++) 
	if (A.find(alf[i])==string::npos) 
	A.push_back(alf[i]);
	return A;
}
int main(){
	string dBth,name,a,password,strP;
	cout<< "Date of birthday(ex.31121999):\n";
	cin >> dBth;
	cout<< "Name:\n";
	cin >> name;
	a = alp(dBth+name);
	cout<<"Password:\n";
	cin >> password;
	long long begin = clock();
	int A[8]={0,0,0,0,0,0,0,0};
	for (A[0]=0;A[0]<a.size();A[0]++)
	for (A[1]=0;A[1]<a.size();A[1]++)
	for (A[2]=0;A[2]<a.size();A[2]++)
	for (A[3]=0;A[3]<a.size();A[3]++)
	for (A[4]=0;A[4]<a.size();A[4]++)
	for (A[5]=0;A[5]<a.size();A[5]++)
	for (A[6]=0;A[6]<a.size();A[6]++)
	for (A[7]=0;A[7]<a.size();A[7]++) {
		strP = "";
		for (int i=0;i<8;i++)
		strP.push_back(a[A[i]]);
		///cout << strP << "\n";
		if (strP==password) {
			long long end = clock();
			cout<<"Time:"<<(end-begin)/CLOCKS_PER_SEC<<"sec\n";
			return 0;

		}
	}
	return 1;
}
